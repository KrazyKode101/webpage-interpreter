import sys

webpage3 = """<html>
<h1>
hello world!
</h1>
<h2>JavaScript That Produces HTML</h2>
<p>
This paragraph starts in HTML ...
<script type="text/javascript">
</script> 
... and this paragraph finishes in HTML. 
</p> 
</html>
"""

webpage1 = """<html>
<h1>JavaScript That Produces HTML</h1>
<p>
This paragraph starts in HTML ...
<script type="text/javascript">
write("<b>This whole sentence should be bold, and the concepts in this problem touch on the 
<a href='http://en.wikipedia.org/wiki/Document_Object_Model'>Document Object Model</a>, 
which allows web browsers and scripts to <i>manipulate</i> webpages.</b>");
</script> 
... and this paragraph finishes in HTML. 
</p> 
<hr> </hr> <!-- draw a horizontal bar --> 
<p> 
Now we will use JavaScript to display even numbers in <i>italics</i> and
odd numbers in <b>bold</b>. <br> </br> 
<script type="text/javascript">
function tricky(i) {
  if (i <= 0) {
    return i; 
  };
  return tricky(i - 1); 
}
tricky(10);
</script> 
</p> 
</html>"""

webpage2 = """<html>
<h1>
Hi Udacity,
</h1>
<h2>
Thanks a lot!
</h2>
<p>
I enjoyed a lot working in this course.
I owe you guys for lifetime.
</p>
<script type="text/javascript">
var i = 10;
while(i > 2)
{
  i = i - 1;
  write("<p>thank you!</p>");
};
</script>
<p>
<big><b><i>Keep Rocking</i></b></big>
</p>
</html>
"""