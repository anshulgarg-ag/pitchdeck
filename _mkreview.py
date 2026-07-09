src = r'C:\suvijya\projects\pitchdeck\pitch-deck-email.html'
dst = r'C:\suvijya\projects\pitchdeck\_review.html'
s = open(src, encoding='utf-8').read()
inject = """
<script>(function(){ var h = parseInt(location.hash.slice(1)); if(!isNaN(h)){ i = h; render(); } })();</script>
<style> .nav,.counter{display:none !important;} </style>
"""
open(dst, 'w', encoding='utf-8').write(s.replace('</body>', inject + '\n</body>'))
print('ok')
