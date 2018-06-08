graph_template = '''
digraph {

graph[
	label=":)",
	overlap=false;
	splines=polyline;
	sep=.5
]

graph [splines=ortho, nodesep=0]
node [shape=record]

%s

}
'''