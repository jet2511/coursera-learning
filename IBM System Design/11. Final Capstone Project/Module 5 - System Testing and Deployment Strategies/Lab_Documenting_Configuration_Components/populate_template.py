import docx

src_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Documenting_Configuration_Components\Template.docx"
out_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Documenting_Configuration_Components\Completed_Template_Documenting_configuration_for_solution_components.docx"

doc = docx.Document(src_path)

# Task 1: Table 0 (Inventory of Components)
t0 = doc.tables[0]
task1_data = [
    ("PostgreSQL Database", "Core ACID transaction ledger, balances, and customer accounts", "Dev, Test, Prod", "Y", "Requires connection pooling, TLS 1.3 certs, WAL archiving, and memory tuning."),
    ("Kong API Gateway", "Ingress traffic routing, rate limiting, OAuth2 validation, and CORS", "Dev, Test, Prod", "Y", "Configures declarative routes, rate limiting tiers, and mTLS plugins."),
    ("Keycloak IAM", "Centralized IAM, OAuth2/OIDC token issuance, MFA, and RBAC", "Dev, Test, Prod", "Y", "Requires realm setup, token lifespans, brute-force protection, and LDAP sync."),
    ("Nginx / ALB Load Balancer", "Layer 7 SSL termination, edge DDoS buffering, and reverse proxy routing", "Dev, Test, Prod", "Y", "Configures upstream health checks, HTTP/2 enforcement, and cipher hardening."),
    ("GitHub Actions CI/CD", "Automated build, DevSecOps security gating (SAST/Trivy), and deployment", "Dev, Test, Prod", "Y", "Pipeline environment secrets, runner IAM roles, and approval gates."),
    ("Prometheus & Alertmanager", "Real-time Golden Signals monitoring, alerting rule evaluation, PagerDuty", "Dev, Test, Prod", "Y", "Custom scraping intervals, P1/P2 alert thresholds, and notification routing.")
]

for idx, data in enumerate(task1_data):
    if idx + 1 < len(t0.rows):
        row = t0.rows[idx + 1]
    else:
        row = t0.add_row()
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 2: Component 1 (PostgreSQL) in Template Paragraphs & Table 1
for i, p in enumerate(doc.paragraphs):
    if "Component 1:" in p.text:
        p.text = "Component 1: PostgreSQL Core Banking Database"
    elif p.text.startswith("(Insert CLI commands/installation notes)"):
        p.text = "Installation steps:\n1. Update repos: sudo apt-get update && sudo apt-get install -y postgresql-16 postgresql-contrib-16\n2. Initialize cluster with checksums: sudo -u postgres /usr/lib/postgresql/16/bin/initdb -D /var/lib/postgresql/16/main --data-checksums\n3. Enable and start service: sudo systemctl enable postgresql && sudo systemctl start postgresql"
    elif p.text.startswith("KEY1="):
        p.text = "POSTGRES_DB=retail_bank_ledger\nPOSTGRES_USER=app_banking_admin\nPOSTGRES_PASSWORD_FILE=/run/secrets/pg_ledger_pwd\nPOSTGRES_PORT=5432\nPOSTGRES_MAX_CONNECTIONS=200\nPOSTGRES_SSL_MODE=verify-full"
    elif p.text.startswith("KEY2=") or p.text.startswith("PORT="):
        p.text = "" # Cleared as merged into above
    elif p.text.startswith("Filename:"):
        p.text = "Filename: postgresql.conf & pg_hba.conf"
    elif p.text.startswith("Location:"):
        p.text = "Location: /etc/postgresql/16/main/"
    elif p.text.startswith("Required parameters:"):
        p.text = "Required parameters: listen_addresses = '*', ssl = on, ssl_min_protocol_version = 'TLSv1.3', password_encryption = scram-sha-256, shared_buffers = 8GB, wal_level = logical"

# Table 1: Default vs Custom settings for Component 1
t1 = doc.tables[1]
task2_t1_data = [
    ("ssl", "off", "on", "Enforce TLS 1.3 encryption across all client and replica connections."),
    ("shared_buffers", "128MB", "8GB (25% RAM)", "Cache frequent ledger queries and account lookups in RAM."),
    ("wal_level", "replica", "logical", "Support streaming replication and Kafka Debezium CDC for fraud monitoring."),
    ("password_encryption", "md5", "scram-sha-256", "Comply with PCI-DSS credential hashing standards.")
]
for idx, data in enumerate(task2_t1_data):
    if idx + 1 < len(t1.rows):
        row = t1.rows[idx + 1]
    else:
        row = t1.add_row()
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Table 2: Security Best Practices for Component 1
t2 = doc.tables[2]
t2.rows[0].cells[0].text = """Security Best Practices for PostgreSQL:
- Enforce TLS 1.3 across all client connections; reject unencrypted traffic.
- Transparent Data Encryption (TDE) at rest using AWS KMS / HashiCorp Vault.
- Enforce automated 90-day credential rotation via HashiCorp Vault.
- Restrict network access via pg_hba.conf to private application subnets only."""

# Table 3: Configuration instructions for Components 2 and 3
t3 = doc.tables[3]
t3.rows[0].cells[0].text = """Component 2: Kong API Gateway
1. Installation Steps:
   helm repo add kong https://charts.konghq.com && helm repo update
   helm install kong-gateway kong/kong -n gateway --create-namespace --set env.database=off
2. Environment Variables & Settings:
   KONG_DATABASE=off (Declarative DB-less mode), KONG_PROXY_LISTEN=0.0.0.0:8443 ssl http2, KONG_ADMIN_LISTEN=127.0.0.1:8001
3. Routing & Plugins:
   - Routes: Route /api/v1/payments and /api/v1/onboarding to backend core microservices.
   - Rate Limiting: 60 req/min for anonymous users; 1,000 req/min for authenticated banking users.
   - Authentication: Mandatory JWT / OAuth2 token verification plugin enabled on all routes.
   - CORS: Strictly whitelisted banking origins with Access-Control-Allow-Credentials: true.
4. Security Controls:
   mTLS client verification, automatic stripping of internal headers before dispatch.

-------------------------------------------------------------------------------------

Component 3: Keycloak Identity & Access Management (IAM)
1. Installation Steps:
   podman run -d --name keycloak-iam -p 8443:8443 -v /etc/keycloak/certs:/opt/keycloak/conf/certs:ro quay.io/keycloak/keycloak:24.0.2 start --optimized
2. Environment Variables:
   KC_DB=postgres, KC_DB_URL=jdbc:postgresql://postgres-db:5432/keycloak_iam, KC_HOSTNAME=auth.retailbank.com, KC_HTTPS_CERTIFICATE_FILE=/opt/keycloak/conf/certs/tls.crt
3. Key Configuration Settings:
   - Dedicated 'retail-bank' realm isolated from master realm.
   - Token Policies: Access token lifespan = 5 minutes; Refresh token lifespan = 30 minutes with Single-Use rotation.
   - Mandatory Multi-Factor Authentication (MFA) via TOTP or WebAuthn for high-value transactions.
   - Brute-force protection: Lock account after 5 consecutive failed login attempts for 15 minutes."""

# Table 4: Snippets and Screenshots
t4 = doc.tables[4]
t4.rows[0].cells[0].text = """[1] PostgreSQL Kubernetes StatefulSet Manifest (YAML):
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

[2] Kong Declarative Routing & Plugin Configuration (YAML):
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

[3] Keycloak Client Security Configuration (JSON):
{
  "clientId": "retail-mobile-app",
  "enabled": true,
  "publicClient": true,
  "standardFlowEnabled": true,
  "implicitFlowEnabled": false,
  "redirectUris": ["https://app.retailbank.com/oauth2/callback"],
  "attributes": {
    "pkce.code.challenge.method": "S256",
    "access.token.lifespan": "300"
  }
}"""

# Table 5: Environment-Specific Guidance
t5 = doc.tables[5]
task4_data = [
    ("Dev", "Single-node DB with mock datasets; LOG_LEVEL=DEBUG; relaxed rate limits (10,000/min); mock SMS OTP for MFA.", "No real customer PII permitted; ephemeral secrets in local .env; self-signed TLS allowed; developer VPC isolation."),
    ("Test", "Replicated DB matching production topology; synthetic test data; automated CI/CD deployment; DAST scans active.", "Synthetic data only; TLS 1.3 with internal private CA; secrets injected via Vault; restricted to QA engineers."),
    ("Prod", "Multi-AZ High Availability; connection pooling (PgBouncer); strict rate limiting (1,000/min); 5-minute token TTL.", "Full zero-trust policy; Cloud KMS/HSM secret encryption; PCI-DSS compliance audits enabled; tamper-evident logging; strict RBAC.")
]
for idx, data in enumerate(task4_data):
    row = t5.rows[idx + 1]
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Table 6: Dependency Checks and Version Compatibility
t6 = doc.tables[6]
task5_data = [
    ("PostgreSQL", "v16.2", "Kubernetes v1.29, Linux Kernel v5.15+", "Requires SSD storage (io2) with minimum 3,000 IOPS for ledger transaction throughput."),
    ("Kong API Gateway", "v3.6.1 (Enterprise)", "Kong Ingress Controller v3.1, Helm v3.14", "Compatible with declarative DB-less mode; requires cert-manager for automated TLS renewal."),
    ("Keycloak IAM", "v24.0.2", "OpenJDK 17-JRE, PostgreSQL v16", "Requires reverse proxy headers (X-Forwarded-For, X-Forwarded-Proto) configured at load balancer.")
]
for idx, data in enumerate(task5_data):
    if idx + 1 < len(t6.rows):
        row = t6.rows[idx + 1]
    else:
        row = t6.add_row()
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Table 7: Validation Checklist
t7 = doc.tables[7]
for row in t7.rows[1:]:
    row.cells[1].text = "Yes"

doc.save(out_path)
print("Successfully generated completed docx for Configuration Guides Lab!")
