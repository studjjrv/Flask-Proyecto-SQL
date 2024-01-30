from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app =  Flask (__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

# -----------------------SECCIÓN PARA AGREGAR EN TODAS LAS TABLAS---------------------------
#AGREGAR USUARIOS
@app.route('/nuevo_usuario', methods=['POST'])
def agregarUsuario():
    nombre = request.json['nombre']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO usuarios (Nombre) VALUES (%s)",[nombre])
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Usuario agregado exitosamente'})

#AGREGAR AUTORES
@app.route('/nuevo_autor', methods=['POST'])
def agregarAutor():
    nombre = request.json['nombre']   
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO autores (nombre) VALUES (%s)",[nombre])
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Autor agregado exitosamente'})

#AGREGAR EDITORIALES
@app.route('/nuevo_editorial', methods=['POST'])
def agregarEditorial():
    nombre = request.json['nombre']   
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO editoriales (nombre) VALUES (%s)",[nombre])
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Editorial agregada exitosamente'})

#AGREGAR GENERO
@app.route('/nuevo_genero', methods=['POST'])
def agregarGenero():
    nombre = request.json['nombre']   
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO generos (nombre) VALUES (%s)",[nombre])
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Genero agregado exitosamente'})

#AGREGAR LIBROS
@app.route('/nuevo_libro', methods=['POST'])
def agregarLibro():
    titulo = request.json['titulo']
    anno_publicacion = request.json['anno_publicacion']
    autor_id = request.json['autor_id']
    genero_id = request.json['genero_id']
    editorial_id = request.json['editorial_id']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO libros (titulo, anno_publicacion, autor_id, genero_id,editorial_id) VALUES (%s,%s,%s,%s,%s)",(titulo, anno_publicacion, autor_id, genero_id,editorial_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Libro agregado exitosamente'})

#AGREGAR RESEÑA
@app.route('/nueva_resena', methods=['POST'])
def agregarResena():
    contenido = request.json['contenido']
    libro_id = request.json['libro_id']
    usuario_id = request.json['usuario_id']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO resenas (contenido, libro_id, usuario_id) VALUES (%s,%s,%s)",(contenido, libro_id, usuario_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Libro agregado exitosamente'})

# -----------------------SECCIÓN PARA OBTENER DATOS EN TODAS LAS TABLAS---------------------------

#OBTENER TODOS LOS USUARIOS
@app.route('/usuarios', methods=['GET'])
def obtenerUsuarios():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT *  FROM usuarios")   
    columnas = [columna[0] for columna in cursor.description]
    usuarios = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    respuesta = jsonify(usuarios)
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return respuesta


#OBTENER TODOS LOS AUTORES
@app.route('/autores', methods=['GET'])
def obtenerAutores():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM autores")
    columnas = [columna[0] for columna in cursor.description]
    autores = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()

    respuesta = jsonify(autores)
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return respuesta

#OBTENER TODOS LOS EDITORIALES
@app.route('/editoriales', methods=['GET'])
def obtenerEditoriales():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM editoriales")
    columnas = [columna[0] for columna in cursor.description]
    editoriales = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()

    respuesta = jsonify(editoriales)
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return respuesta

#OBTENER TODOS LOS GENEROS
@app.route('/generos', methods=['GET'])
def obtenerGeneros():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM generos")
    columnas = [columna[0] for columna in cursor.description]
    generos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()

    respuesta = jsonify(generos)
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return respuesta

#OBTENER TODOS LOS LIBROS
@app.route('/libros', methods=['GET'])
def obtenerLibros():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM libros")
    columnas = [columna[0] for columna in cursor.description]
    libros = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()

    respuesta = jsonify(libros)
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return respuesta


#OBTENER TODOS LOS RESEÑAS
@app.route('/resenas', methods=['GET'])
def obtenerResenas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM resenas")
    columnas = [columna[0] for columna in cursor.description]
    resenas = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()

    respuesta = jsonify(resenas)
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return respuesta


# -----------------------SECCIÓN PARA OBTENER DATOS EN TODAS LAS TABLAS POR ID---------------------------

#OBTENER USUARIOS POR ID
@app.route('/usuarios/<usuario_id>', methods=['GET'])
def obtnerUsuarioEspecifico(usuario_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
    columnas = [columna[0] for columna in cursor.description]
    respuesta = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    if respuesta:
        return jsonify(respuesta)
    else:
        return jsonify({'Mensaje':'Usuario no registrado'}),404
    

#OBTENER AUTORES POR ID
@app.route('/autores/<autores_id>', methods=['GET'])
def obtnerAutoresEspecifico(autores_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM autores WHERE id = %s", (autores_id,))
    columnas = [columna[0] for columna in cursor.description]
    respuesta = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    if respuesta:
        return jsonify(respuesta)
    else:
        return jsonify({'Mensaje':'Autor no registrado'}),404

#OBTENER EDITORIALES POR ID
@app.route('/editoriales/<editorial_id>', methods=['GET'])
def obtenerEditorialesEspecificos(editorial_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM editoriales WHERE id = %s", (editorial_id,))
    columnas = [columna[0] for columna in cursor.description]
    respuesta = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    cursor.close()
    if respuesta:
        return jsonify(respuesta)
    else:
        return jsonify({'Mensaje':'Editorial no registrada'}),404

#OBTENER GENEROS POR ID
@app.route('/generos/<genero_id>', methods=['GET'])
def obtenerGenerosEspecificos(genero_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM generos WHERE id = %s",(genero_id,))
    columnas = [columna[0] for columna in cursor.description]
    respuesta = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    if respuesta:
        return jsonify(respuesta)
    else:
        return jsonify({'Mensaje':'Género no registrado'}),404

#OBTENER LIBROS POR ID
@app.route('/libros/<libro_id>', methods=['GET'])
def obtenerLibrosEspecificos(libro_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM libros WHERE id= %s",(libro_id,))
    columnas = [columna[0] for columna in cursor.description]
    respuesta = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    cursor.close()
    if respuesta:
        return jsonify(respuesta)
    else:
        return jsonify({'Mensaje':'Libro no registrado'}),404

#OBTENER RESEÑA POR ID
@app.route('/resenas/<resena_id>', methods=['GET'])
def obtenerResenasEspecificos(resena_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM resenas WHERE id = %s",(resena_id,))
    columnas = [columna[0] for columna in cursor.description]
    respuesta = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    cursor.close()
    if respuesta:
        return jsonify(respuesta)
    else:
        return jsonify({'Mensaje':'Reseña no registrada'}),404


# -----------------------ELIMINAR DATOS POR ID---------------------------
    
#ELIMINAR USUARIO POR ID
@app.route('/usuarios/eliminar/<usuario_id>', methods = ['DELETE'])
def eliminar_usuario(usuario_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Usuario eliminado exitosamente'})

#ELIMINAR AUTORES POR ID
@app.route('/autores/eliminar/<autor_id>', methods = ['DELETE'])
def eliminarAutor(autor_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM autores WHERE id = %s", (autor_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Autor eliminado exitosamente'})

#ELIMINAR EDITORIAL POR ID
@app.route('/editoriales/eliminar/<editorial_id>', methods = ['DELETE'])
def eliminarEditorial(editorial_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM editoriales WHERE id = %s", (editorial_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Editorial eliminada exitosamente'})

#ELIMINAR GENERO POR ID
@app.route('/generos/eliminar/<genero_id>', methods = ['DELETE'])
def eliminarGenero(genero_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM generos WHERE id = %s", (genero_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Género eliminado exitosamente'})

#ELIMINAR LIBROS POR ID
@app.route('/libros/eliminar/<libro_id>', methods = ['DELETE'])
def eliminarLibro(libro_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM libros WHERE id = %s", (libro_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Libro eliminado exitosamente'})

#ELIMINAR LIBROS POR ID
@app.route('/resenas/eliminar/<resena_id>', methods = ['DELETE'])
def eliminarResena(resena_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM resenas WHERE id = %s", (resena_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'Mensaje':'Reseña eliminada exitosamente'})


# -----------------------ACTUALIZAR DATOS POR ID---------------------------


#ACTUALIZAR USUARIO POR ID    
@app.route('/usuarios/actualizar/<usuario_id>', methods = ['PATCH'])
def actualizarUsuario(usuario_id):
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE usuarios SET nombre = %s WHERE id = %s", (nombre, usuario_id))

    mysql.connection.commit()
    cursor.close()

    return jsonify({'Resultado':'El usuario se ha actualizado correctamente'})

#ACTUALIZAR AUTORES POR ID    
@app.route('/autores/actualizar/<autor_id>', methods = ['PATCH'])
def actualizarAutor(autor_id):
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE autores SET nombre = %s WHERE id = %s", (nombre, autor_id))

    mysql.connection.commit()
    cursor.close()

    return jsonify({'Resultado':'El autor se ha actualizado correctamente'})


#ACTUALIZAR EDITORIALES POR ID    
@app.route('/editoriales/actualizar/<editorial_id>', methods = ['PATCH'])
def actualizarEditorial(editorial_id):
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE editoriales SET nombre = %s WHERE id = %s", (nombre, editorial_id))

    mysql.connection.commit()
    cursor.close()

    return jsonify({'Resultado':'El editorial se ha actualizado correctamente'})


#ACTUALIZAR EDITORIALES POR ID    
@app.route('/generos/actualizar/<genero_id>', methods = ['PATCH'])
def actualizarGenero(genero_id):
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE generos SET nombre = %s WHERE id = %s", (nombre, genero_id))

    mysql.connection.commit()
    cursor.close()

    return jsonify({'Resultado':'El género se ha actualizado correctamente'})

#ACTUALIZAR LIBROS POR ID    
@app.route("/libros/actualizar/<libro_id>", methods=["PATCH"])
def actualizarLibros(libro_id):
    datos_actualizados = request.json

    if not datos_actualizados:
        return jsonify({"Error":"No se enviaron los datos"})

    cursor = mysql.connection.cursor()
    update_query = "UPDATE libros SET "
    update_data = []

    for campo, valor in datos_actualizados.items():
        if campo in ["titulo","apellido","anno_publicacion","autor_id","genero_id","editorial_id"]:
            update_query += f"{campo} = %s, " 
            update_data.append(valor) 
    if not update_data:
        return jsonify({"Error":"Los datos estan vacios!"})
    
    update_query = update_query.rstrip(', ')
    update_query += " WHERE id = %s"
    update_data.append(libro_id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'resultado':'El libro se actualizo correctamente!'})


#ACTUALIZAR RESEÑAS POR ID    
@app.route("/resenas/actualizar/<resenas_id>", methods=["PATCH"])
def actualizarResenas(resenas_id):
    datos_actualizados = request.json

    if not datos_actualizados:
        return jsonify({"Error":"No se enviaron los datos"})

    cursor = mysql.connection.cursor()
    update_query = "UPDATE resenas SET "
    update_data = []

    for campo, valor in datos_actualizados.items():
        if campo in ["contenido","libro_id","usuario_id"]:
            update_query += f"{campo} = %s, " 
            update_data.append(valor) 
    if not update_data:
        return jsonify({"Error":"Los datos estan vacios!"})
    
    update_query = update_query.rstrip(', ')
    update_query += " WHERE id = %s"
    update_data.append(resenas_id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'resultado':'La reseña se actualizo correctamente!'})

# -----------------------MOSTRAR UN GET CON UNA CONSULTA EN ESPECÍFICO ---------------------------

@app.route('/consulta/general', methods=['GET'])
def obtenerConsultageneral():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT libros.id as "ID Libro", libros.titulo as "Nombre del libro", autores.nombre as "Nombre del Autor", generos.nombre as "Nombre del Género", resenas.contenido as "Reseña", usuarios.nombre as "Nombre de Usuario" FROM libros INNER JOIN autores ON autores.id = libros.autor_id INNER JOIN generos on generos.id = libros.genero_id INNER JOIN resenas on resenas.libro_id = libros.id INNER JOIN usuarios on usuarios.id = resenas.usuario_id ORDER by 1')
    columnas = [columna[0] for columna in cursor.description]
    respuesta = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    if respuesta:
        return jsonify(respuesta)
    else:
        return jsonify({'Mensaje':'No se encontraron datos a tu petición'}),404

if __name__ == '__main__':
    app.run(debug=True, port=8080)