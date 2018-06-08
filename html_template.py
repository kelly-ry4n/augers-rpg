html_template = '''<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Herald</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link rel="stylesheet" href="css/styles.css?v=1.0">


</head>
<style>
body {
	margin: 20px;
}
</style>

<body>
	<a href="full_graph.svg"><h1>Skill Tree</h1></a>
	Hover nodes for skill descriptions<br/>
	Nodes are links to appropriate place in skill list<br/>


	<a href="rules.html"><h1>Game Rules</h1></a><br/>


	%s

</body>
</html>'''