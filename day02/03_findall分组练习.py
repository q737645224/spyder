import re

s = """<div class="animal">
  <p class="name">
    <a title="Tiger"></a>
  </p>

  <p class="contents">
    Two tigers two tigers run fast 
  </p>
</div>

<div class="animal">
  <p class="name">
    <a title="Rabbit"></a>
  </p>

  <p class="contents">
    Small white rabbit white and white  
  </p>
</div>"""
p = re.compile('<div class="animal">.*?title="(.*?)".*?class="contents">\s+(.*?)\s+</p>.*?</div>',re.S)
result = p.findall(s)
for m in result:
    print("动物名称:",m[0].strip())
    print("动物描述:",m[1].strip())
    print("*" * 30)






