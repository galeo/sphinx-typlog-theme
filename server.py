from livereload import Server, shell

server = Server()
server.watch('src/css/*', shell('npm run build:css'))
server.watch('src/*.js', shell('npm run build:js'))
server.watch('docs/*', shell('make docs'))
server.serve(root='docs/_build/html', port=5234)
server.watch('sphinx_typlog_dark_theme/*', shell('make docs'))
server.watch('sphinx_typlog_dark_theme/static/*', shell('make docs'))
