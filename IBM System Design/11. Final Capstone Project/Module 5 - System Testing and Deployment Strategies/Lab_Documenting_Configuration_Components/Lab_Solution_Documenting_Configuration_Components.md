# Lab: Documenting Configuration for Solution Components - Solution

**Course:** IBM System Design - Capstone Project  
**Module:** Module 5 - System Testing and Deployment Strategies  
**Target System:** Retail Bank Digital Core Platform (Onboarding, Payments, Loans, Fraud/AML, Identity)  
**Author:** Parikshit Jain  

---

## Task 1: Identify Components Requiring Configuration

Comprehensive inventory of core banking solution components requiring configuration:

| Component | Purpose | Environment (Dev/Test/Prod) | Needs Configuration? (Y/N) | Notes |
| :--- | :--- | :--- | :---: | :--- |
| **PostgreSQL Database** | Core ACID transaction ledger, account balances, and customer financial records. | Dev, Test, Prod | **Y** | Requires connection pooling, TLS 1.3 certificates, WAL archiving, and custom memory tuning. |
| **Kong API Gateway** | Central ingress traffic routing, rate limiting, OAuth2 token validation, and CORS. | Dev, Test, Prod | **Y** | Configures declarative service routes, rate-limiting tiers, and mutual TLS plugins. |
| **Keycloak Identity Provider** | Centralized IAM, OAuth2/OIDC token issuance, MFA enforcement, and RBAC policies. | Dev, Test, Prod | **Y** | Requires realm setup, token expiration timeouts, brute-force protection, and LDAP sync. |
| **Nginx / Cloud Load Balancer** | Layer 7 SSL termination, edge DDoS buffering, and reverse proxy routing to API gateways. | Dev, Test, Prod | **Y** | Configures upstream health checks, HTTP/2 enforcement, and cipher suite hardening. |
| **GitHub Actions / CI/CD Runner** | Automated build, DevSecOps security gating (SAST/Trivy), and deployment automation. | Dev, Test, Prod | **Y** | Pipeline environment secrets, runner IAM permissions, and CAB approval gates. |
| **Prometheus & Alertmanager** | Real-time Golden Signals monitoring, alerting rule evaluation, and PagerDuty integration. | Dev, Test, Prod | **Y** | Custom scraping intervals, P1/P2 alert thresholds, and notification routing configs. |

---

## Task 2: Document Configuration Instructions for 3 Components

### Component 1: PostgreSQL Core Banking Database

#### 1. Installation Steps
```bash
# Ubuntu / Debian clean installation
sudo apt-get update && sudo apt-get install -y postgresql-16 postgresql-contrib-16
# Initialize database cluster with data checksums enabled (vital for banking integrity)
sudo -u postgres /usr/lib/postgresql/16/bin/initdb -D /var/lib/postgresql/16/main --data-checksums
# Enable and start PostgreSQL daemon
sudo systemctl enable postgresql && sudo systemctl start postgresql
```

#### 2. Environment Variables (`.env`)
```bash
POSTGRES_DB=retail_bank_ledger
POSTGRES_USER=app_banking_admin
POSTGRES_PASSWORD_FILE=/run/secrets/pg_ledger_pwd   # Injected via Vault
POSTGRES_PORT=5432
POSTGRES_MAX_CONNECTIONS=200
POSTGRES_SSL_MODE=verify-full
POSTGRES_SSL_CERT=/etc/ssl/certs/db-cert.crt
POSTGRES_SSL_KEY=/etc/ssl/private/db-key.key
```

#### 3. Default vs. Custom Settings
| Setting | Default | Custom | Reason |
| :--- | :--- | :--- | :--- |
| `ssl` | `off` | `on` | Enforce TLS 1.3 encryption across all client and replica connections. |
| `shared_buffers` | `128MB` | `8GB` (25% RAM) | Cache frequent ledger queries and account lookups in RAM. |
| `wal_level` | `replica` | `logical` | Support both streaming replication and Kafka Debezium CDC for fraud monitoring. |
| `password_encryption` | `md5` | `scram-sha-256` | Comply with PCI-DSS credential hashing standards. |

#### 4. Security Best Practices
- Require TLS 1.3 for all database connections (`ssl_min_protocol_version = 'TLSv1.3'`).
- Enable transparent data encryption (TDE) at rest using AWS KMS / HashiCorp Vault.
- Enforce quarterly 90-day automated credential rotation.
- Restrict remote network access via `pg_hba.conf` to API Gateway and backend subnets only.

#### 5. Configuration File References
- **Filename:** `postgresql.conf` & `pg_hba.conf`
- **Location:** `/etc/postgresql/16/main/`
- **Required Parameters:** `listen_addresses = '*'`, `ssl = on`, `ssl_ca_file = 'root.crt'`, `archive_mode = on`.

---

### Component 2: Kong API Gateway

#### 1. Installation Steps
```bash
# Install Kong Gateway Enterprise via Helm on Kubernetes
helm repo add kong https://charts.konghq.com && helm repo update
helm install kong-gateway kong/kong -n gateway --create-namespace \
  --set env.database=off \
  --set env.declarative_config=/etc/kong/kong.yml
```

#### 2. Environment Variables & Key Settings
```bash
KONG_DATABASE=off                           # Declarative DB-less mode
KONG_DECLARATIVE_CONFIG=/etc/kong/kong.yml
KONG_PROXY_LISTEN=0.0.0.0:8443 ssl http2
KONG_ADMIN_LISTEN=127.0.0.1:8001            # Bound to localhost only
KONG_PLUGINS=bundled,rate-limiting,jwt,cors,prometheus
```

#### 3. Route, Authentication & Rate Limiting Configuration
- **Route Definitions:** Map incoming `/api/v1/payments` and `/api/v1/onboarding` to internal backend services.
- **Authentication:** Enforce JWT / OAuth2 validation on all external endpoints.
- **Rate Limiting:** Protect backend core services by restricting unauthenticated callers to 60 req/min and authenticated banking users to 1,000 req/min.
- **CORS Configuration:** Explicitly allow approved banking web/mobile client origins with `Access-Control-Allow-Credentials: true`.

#### 4. Security Controls
- Terminate mTLS between external clients and Kong.
- Strip internal headers (`X-Consumer-ID`, `X-Internal-Token`) prior to external response dispatch.

---

### Component 3: Keycloak Identity & Access Management (IAM)

#### 1. Installation Steps
```bash
# Production Keycloak deployment using container image
podman run -d --name keycloak-iam -p 8443:8443 \
  -v /etc/keycloak/certs:/opt/keycloak/conf/certs:ro \
  quay.io/keycloak/keycloak:24.0.2 start --optimized
```

#### 2. Environment Variables (`.env`)
```bash
KC_DB=postgres
KC_DB_URL=jdbc:postgresql://postgres-db:5432/keycloak_iam
KC_DB_USERNAME=keycloak_user
KC_DB_PASSWORD_FILE=/run/secrets/keycloak_db_pwd
KC_HOSTNAME=auth.retailbank.com
KC_HTTPS_CERTIFICATE_FILE=/opt/keycloak/conf/certs/tls.crt
KC_HTTPS_CERTIFICATE_KEY_FILE=/opt/keycloak/conf/certs/tls.key
```

#### 3. Key Configuration Settings
- **Realm Configuration:** Create dedicated `retail-bank` realm isolated from master realm.
- **Token Policies:** Access token lifespan = 5 minutes; Refresh token lifespan = 30 minutes with Single-Use rotation.
- **MFA Enforcement:** Mandatory TOTP (Google Authenticator) or WebAuthn/FIDO2 for all customer fund transfers.
- **Brute Force Protection:** Lock account after 5 consecutive failed login attempts for 15 minutes.

---

## Task 3: Add Configuration Snippets and Artifacts

### 1. PostgreSQL Declarative Kubernetes Secret & Deployment (`postgresql.yaml`)
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres-ledger
  namespace: banking-core
spec:
  serviceName: postgres-ledger
  replicas: 1
  template:
    spec:
      containers:
        - name: postgres
          image: postgres:16-alpine
          ports:
            - containerPort: 5432
          env:
            - name: POSTGRES_DB
              value: "retail_bank_ledger"
            - name: POSTGRES_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-vault-credentials
                  key: password
          volumeMounts:
            - name: postgres-data
              mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
    - metadata:
        name: postgres-data
      spec:
        accessModes: [ "ReadWriteOnce" ]
        resources:
          requests:
            storage: 250Gi
```

### 2. Kong Gateway Declarative Configuration (`kong.yml`)
```yaml
_format_version: "3.0"
services:
  - name: payment-service
    url: http://payment-service.banking-core.svc.cluster.local:8080
    routes:
      - name: payment-route
        paths:
          - /api/v1/payments
        strip_path: false
        protocols:
          - https
    plugins:
      - name: rate-limiting
        config:
          minute: 1000
          policy: local
      - name: jwt
        config:
          claims_to_verify:
            - exp
```

### 3. Keycloak Client Configuration Policy (`keycloak-client.json`)
```json
{
  "clientId": "retail-mobile-app",
  "enabled": true,
  "publicClient": true,
  "standardFlowEnabled": true,
  "implicitFlowEnabled": false,
  "directAccessGrantsEnabled": false,
  "redirectUris": [
    "https://app.retailbank.com/oauth2/callback",
    "retailbank://auth/callback"
  ],
  "attributes": {
    "pkce.code.challenge.method": "S256",
    "access.token.lifespan": "300"
  }
}
```

---

## Task 4: Environment-Specific Guidance

| Environment | Configuration Differences | Security Notes |
| :--- | :--- | :--- |
| **Development (Dev)** | Single-node PostgreSQL with mock financial datasets; debug logging enabled (`LOG_LEVEL=DEBUG`); Kong rate-limiting relaxed (10,000 req/min); mock SMS OTP for MFA. | No real customer PII permitted; ephemeral secrets allowed in local developer `.env`; TLS verification can be self-signed; isolated in developer VPC. |
| **Testing (Test/QA)** | Replicated database matching production topology; synthetic test data generated by automation; automated CI/CD pipeline triggers test suites; DAST scans active. | Synthetic data only; TLS 1.3 enforced using internal private CA certificates; credentials injected via test secret vault; access restricted to QA engineers. |
| **Production (Prod)** | Multi-AZ High Availability with active read-replicas; connection pooling (PgBouncer); strict rate limiting (1,000 req/min); strict 5-minute token TTL. | Full zero-trust network policy; mandatory Cloud KMS/HSM secret encryption; PCI-DSS compliance audits enabled; tamper-evident audit logging; strict RBAC. |

---

## Task 5: Dependency Checks and Version Compatibility

| Component | Required Version | Verified Against | Notes |
| :--- | :--- | :--- | :--- |
| **PostgreSQL** | `v16.2` | Kubernetes `v1.29`, Linux Kernel `v5.15+` | Requires SSD storage (io2) with minimum 3,000 IOPS for transaction ledger throughput. |
| **Kong API Gateway** | `v3.6.1` (Enterprise) | Kong Ingress Controller `v3.1`, Helm `v3.14` | Compatible with declarative DB-less mode; requires cert-manager for automated TLS renewal. |
| **Keycloak IAM** | `v24.0.2` | OpenJDK `17-JRE`, PostgreSQL `v16` | Requires HTTPS reverse proxy headers (`X-Forwarded-For`, `X-Forwarded-Proto`) configured at load balancer. |

---

## Task 6: Validate Checklist

| Validation Item | Yes/No | Verification Evidence |
| :--- | :---: | :--- |
| **Components fully identified** | **Yes** | 6 essential banking components (DB, API Gateway, IAM, LB, CI/CD, Monitoring) categorized in Task 1. |
| **Config steps are complete** | **Yes** | Installation, environment variables, default vs custom values, and security steps written for DB, Gateway, and IAM. |
| **Environment variables documented** | **Yes** | Complete `.env` variables documented with secure Vault secret referencing. |
| **Code/config snippets included** | **Yes** | Reproducible Kubernetes YAML, Kong declarative YAML, and Keycloak JSON policies provided in Task 3. |
| **Default vs override settings explained** | **Yes** | Documented custom parameters (e.g., `shared_buffers`, `wal_level`, `rate-limiting`) with technical justifications. |
| **Security considerations included** | **Yes** | Enforced TLS 1.3, SCRAM-SHA-256, 90-day credential rotation, PKCE S256, and PCI-DSS compliance. |
| **Version compatibility documented** | **Yes** | Matrix of component versions and target platform compatibility established in Task 5. |
| **Instructions reproducible in a clean environment** | **Yes** | Standard CLI installation commands and declarative manifests verify end-to-end reproducibility. |
