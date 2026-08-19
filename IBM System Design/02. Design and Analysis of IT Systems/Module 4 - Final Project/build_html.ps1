$mdContent = Get-Content -Raw -Encoding UTF8 "Final_Project_Submission_Document.md"

$htmlHeader = @"
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Final Project Submission - Digital Transformation Strategy</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<style>
  @page {
    size: A4;
    margin: 15mm;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.5;
    color: #1a1a1a;
    max-width: 850px;
    margin: 0 auto;
    padding: 20px;
    font-size: 13px;
  }
  h1 { font-size: 22px; border-bottom: 2px solid #0969da; padding-bottom: 8px; color: #0969da; margin-top: 0; }
  h2 { font-size: 17px; border-bottom: 1px solid #d0d7de; padding-bottom: 6px; margin-top: 24px; color: #1f2328; page-break-after: avoid; }
  h3 { font-size: 14px; margin-top: 18px; color: #24292f; page-break-after: avoid; }
  h4 { font-size: 13px; margin-top: 14px; color: #57606a; page-break-after: avoid; }
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 14px 0;
    font-size: 12px;
    page-break-inside: avoid;
  }
  th, td {
    border: 1px solid #d0d7de;
    padding: 6px 10px;
    vertical-align: top;
  }
  th {
    background-color: #f6f8fa;
    font-weight: 600;
    text-align: left;
  }
  tr:nth-child(even) { background-color: #fcfcfc; }
  code {
    background-color: #f6f8fa;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 90%;
  }
  .mermaid {
    text-align: center;
    margin: 18px 0;
    page-break-inside: avoid;
  }
  ul, ol {
    padding-left: 20px;
    margin: 6px 0;
  }
  li { margin-bottom: 4px; }
  p { margin: 6px 0; }
  hr {
    border: 0;
    border-top: 1px solid #d0d7de;
    margin: 20px 0;
  }
</style>
</head>
<body>
<div id="content"></div>
<script id="raw-md" type="text/plain">
"@

$htmlFooter = @"
</script>
<script>
  mermaid.initialize({ startOnLoad: false, theme: 'default' });
  const raw = document.getElementById('raw-md').textContent;
  
  const renderer = new marked.Renderer();
  const originalCode = renderer.code.bind(renderer);
  renderer.code = function(token) {
    var code = token.text || token;
    var lang = token.lang || '';
    if (lang === 'mermaid') {
      return '<div class="mermaid">' + code + '</div>';
    }
    return originalCode(token);
  };
  
  document.getElementById('content').innerHTML = marked.parse(raw, { renderer: renderer });
  mermaid.run();
</script>
</body>
</html>
"@

$finalHtml = $htmlHeader + "`n" + $mdContent + "`n" + $htmlFooter
$finalHtml | Set-Content -Path "Final_Project_Document.html" -Encoding UTF8
Write-Host "Generated Final_Project_Document.html successfully."
