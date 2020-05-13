import psycopg2

conn = psycopg2.connect(host="localhost",database="PetinShop",
                        user="postgres",password="root")

cur = conn.cursor()

opcionMenuPrincipal = 8
while opcionMenuPrincipal != 0:
    if opcionMenuPrincipal == 1:
        opcionSubmenu = 6
        while opcionSubmenu != 0:
            if opcionSubmenu == 1:
                consulta = 'select *, (select count(fk_id_cliente) from cliente_vendedor_venta where fk_id_cliente = cliente.id_Cliente)as total from cliente;'
                cur.execute(consulta)

                filas = cur.fetchall()

                for r in filas:
                    print('--->ID CLIENTE: ', r[0], '\n     Nombre ', r[1]," ", r[2],'\n     DNI: ', r[3],"\n     Dirección: ",r[4],"\n     Teléfono: ",r[5],"\n     Compras realizadas: ",r[6])
            if opcionSubmenu == 2:
                nombre = str(input("Introduce nombre: "))
                apellidos = str(input("Introduce apellidos: "))
                dni = str(input("Introduce dni: "))
                direccion = str(input("Introduce dirección: "))
                telefono = int(input("Introduce teléfono: "))
                consulta = "SELECT * from Cliente where dni = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    consulta = 'INSERT INTO Cliente (nombre, apellidos, dni, direccion, telefono) VALUES (%s,%s,%s,%s,%s);'
                    val = (nombre,apellidos,dni,direccion,telefono)
                    cur.execute(consulta,val)
                    conn.commit()
                    print("CLIENTE AÑADIDO CON EXITO")
                else:
                    print("Ya existe un cliente con ese DNI")
            if opcionSubmenu == 3:
                dni = str(input("Introduce dni del cliente al que vas a modificar los datos: "))
                consulta = "SELECT * from Cliente where dni = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun cliente con ese DNI")
                else:
                    modificar = str(input("¿Cambiar nombre?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = str(input("Introduce nuevo nombre: "))
                        consulta = 'UPDATE cliente set nombre = %s where dni=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar apellido?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        apellidos = str(input("Introduce nuevo apellidos: "))
                        consulta = 'UPDATE cliente set apellidos = %s where dni=%s'
                        val = (apellidos, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar direccion?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        direccion = str(input("Introduce nueva direccion: "))
                        consulta = 'UPDATE cliente set direccion = %s where dni=%s'
                        val = (direccion, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar telefono?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        telefono = int(input("Introduce nuevo telefono: "))
                        consulta = 'UPDATE cliente set telefono = %s where dni=%s'
                        val = (telefono, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    print("CLIENTE MODIFICADO CON EXITO")
            if opcionSubmenu == 4:
                id = str(input("Introduce id del cliente que quieres borrar: "))
                consulta = "SELECT * from Cliente where id_cliente = '{0}'".format(id)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun cliente con ese ID")
                else:
                    try:
                        consulta = "DELETE from Cliente where id_cliente = {0}".format(id)
                        cur.execute(consulta)
                        filas = cur.fetchall()
                        print("CLIENTE BORRADO CON EXITO")
                    except:
                        print("El cliente no se puede borrar porque tiene ventas a su nombre")
            if opcionSubmenu == 5:
                dni = str(input("Introduce dni del cliente que quieres borrar: "))
                consulta = "SELECT * from Cliente where id = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun cliente con ese DNI")
                else:
                    try:
                        consulta = "DELETE from Cliente where dni = {0}".format(dni)
                        cur.execute(consulta)
                        filas = cur.fetchall()
                        print("CLIENTE BORRADO CON EXITO")
                    except:
                        print("El cliente no se puede borrar porque tiene ventas a su nombre")
            submenu = "\n------------------------------\n"
            submenu +="    (1) Mostrar clientes.\n"
            submenu +="    (2) Nuevo cliente.\n"
            submenu +="    (3) Modificar cliente.\n"
            submenu +="    (4) Borrar por ID.\n"
            submenu +="    (5) Borrar por DNI.\n"
            submenu +="        (0) Atrás\n\n    Elige una opción:"
            opcionSubmenu = int(input(submenu))
            print("\n------------------------------\n")
    if opcionMenuPrincipal == 2:
        opcionSubmenu = 6
        while opcionSubmenu != 0:
            if opcionSubmenu == 1:
                consulta = 'select * from proveedor;'
                cur.execute(consulta)

                filas = cur.fetchall()

                for r in filas:
                    print('--->ID PROVEEDOR: ', r[0], '\n     Empresa ', r[1],'\n     CIF: ', r[3],"\n     Dirección: ",r[4])
            if opcionSubmenu == 2:
                nombre = str(input("Introduce nombre de la empresa: "))
                dni = str(input("Introduce CIF: "))
                direccion = str(input("Introduce dirección: "))
                consulta = "SELECT * from Proveedor where cif = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    consulta = 'INSERT INTO Proveedor (empresa, cif, direccion) VALUES (%s,%s,%s);'
                    val = (nombre,dni,direccion)
                    cur.execute(consulta,val)
                    conn.commit()
                    print("PROVEEDOR AÑADIDO CON EXITO")
                else:
                    print("Ya existe un proveedor con ese CIF")
            if opcionSubmenu == 3:
                dni = str(input("Introduce cif del proveedor al que vas a modificar los datos: "))
                consulta = "SELECT * from Proveedor where cif = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun proveedor con ese CIF")
                else:
                    modificar = str(input("¿Cambiar nombre de empresa?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = str(input("Introduce nuevo nombre de empresa: "))
                        consulta = 'UPDATE proveedor set empresa = %s where cif=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar direccion?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        direccion = str(input("Introduce nueva direccion: "))
                        consulta = 'UPDATE proveedor set direccion = %s where cif=%s'
                        val = (direccion, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    print("PROVEEDOR MODIFICADO CON EXITO")
            if opcionSubmenu == 4:
                id = str(input("Introduce id del proveedor que quieres borrar: "))
                consulta = "SELECT * from proveedor where id_proveedor = '{0}'".format(id)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun proveedor con ese ID")
                else:
                    try:
                        consulta = "DELETE from proveedor where id_proveedor = {0}".format(id)
                        cur.execute(consulta)
                        filas = cur.fetchall()
                        print("PROVEEDOR BORRADO CON EXITO")
                    except:
                        print("El proveedor no se puede borrar porque tiene ventas realizadas")
            if opcionSubmenu == 5:
                dni = str(input("Introduce cif del proveedor que quieres borrar: "))
                consulta = "SELECT * from proveedor where cif = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun proveedor con ese CIF")
                else:
                    try:
                        consulta = "DELETE from proveedor where cif = {0}".format(dni)
                        cur.execute(consulta)
                        filas = cur.fetchall()
                        print("PROVEEDOR BORRADO CON EXITO")
                    except:
                        print("El proveedor no se puede borrar porque tiene ventas realizadas")
            submenu = "\n------------------------------\n"
            submenu +="    (1) Mostrar proveedores.\n"
            submenu +="    (2) Nuevo proveedor.\n"
            submenu +="    (3) Modificar proveedor.\n"
            submenu +="    (4) Borrar por ID.\n"
            submenu +="    (5) Borrar por CIF.\n"
            submenu +="        (0) Atrás\n\n    Elige una opción:"
            opcionSubmenu = int(input(submenu))
            print("\n------------------------------\n")
    if opcionMenuPrincipal == 3:
        opcionSubmenu = 6
        while opcionSubmenu != 0:
            if opcionSubmenu == 1:
                consulta = 'select *, (select count(fk_id_vendedor) from cliente_vendedor_venta where fk_id_vendedor = vendedor.id_vendedor)as total,(select sueldo.total from sueldo where vendedor.fk_id_sueldo=id_sueldo)as sueldo from vendedor;'
                cur.execute(consulta)

                filas = cur.fetchall()

                for r in filas:
                    print('--->ID VENDEDOR: ', r[0], '\n     Nombre ', r[1]," ", r[2],'\n     DNI: ', r[3],"\n     Dirección: ",r[4],"\n     Teléfono: ",r[5],"\n     Compras realizadas: ",r[7],"\n     Sueldo: ",r[8])
            if opcionSubmenu == 2:
                nombre = str(input("Introduce nombre: "))
                apellidos = str(input("Introduce apellidos: "))
                dni = str(input("Introduce DNI: "))
                direccion = str(input("Introduce dirección: "))
                telefono = str(input("Introduce teléfono: "))
                base = int(input("Introduce base del sueldo: "))
                comisiones = int(input("Introduce comisiones del sueldo: "))
                consulta = "SELECT * from vendedor where dni = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    consulta = 'INSERT INTO Sueldo (base,comisiones,total) VALUES (%s,%s,%s);'
                    val = (base, comisiones, (base+comisiones))
                    cur.execute(consulta,val)
                    conn.commit()
                    consulta = 'SELECT id_sueldo from sueldo;'
                    cur.execute(consulta)
                    filas = cur.fetchall()
                    id_sueldo=0
                    for r in filas:
                        id_sueldo = r[0]
                    consulta = 'INSERT INTO Vendedor (nombre, apellidos, dni, direccion, telefono,fk_id_Sueldo) VALUES (%s,%s,%s,%s,%s,%s);'
                    val = (nombre,apellidos, dni,direccion,telefono, id_sueldo)
                    cur.execute(consulta,val)
                    conn.commit()
                    print("VENDEDOR AÑADIDO CON EXITO")
                else:
                    print("Ya existe un vendedor con ese DNI")
            if opcionSubmenu == 3:
                dni = str(input("Introduce DNI del vendedor al que vas a modificar los datos: "))
                consulta = "SELECT * from vendedor where dni = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun vendedor con ese DNI")
                else:
                    modificar = str(input("¿Cambiar nombre?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = str(input("Introduce nuevo nombre: "))
                        consulta = 'UPDATE vendedor set nombre = %s where DNI=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar apellido?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = str(input("Introduce nuevo apellido: "))
                        consulta = 'UPDATE vendedor set apellidos = %s where DNI=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar teléfono?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = int(input("Introduce nuevo teléfono: "))
                        consulta = 'UPDATE vendedor set telefono = %s where DNI=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar direccion?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        direccion = str(input("Introduce nueva direccion: "))
                        consulta = 'UPDATE VENDEDOR set direccion = %s where DNI=%s'
                        val = (direccion, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar sueldo?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = int(input("Introduce nueva base del sueldo: "))
                        consulta = 'update sueldo set base=%s where id_sueldo = (select fk_id_sueldo from vendedor where dni=%s)'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                        nombre2 = int(input("Introduce nuevas comisioniones del sueldo: "))
                        consulta = 'update sueldo set comisiones=%s where id_sueldo = (select fk_id_sueldo from vendedor where dni=%s)'
                        val = (nombre2, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                        totalSueldo = nombre+nombre2
                        consulta = 'update sueldo set total=%s where id_sueldo = (select fk_id_sueldo from vendedor where dni=%s)'
                        val = (totalSueldo, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    print("VENDEDOR MODIFICADO CON EXITO")
            if opcionSubmenu == 4:
                id = str(input("Introduce id del vendedor que quieres borrar: "))
                consulta = "SELECT * from vendedor where id_vendedor = '{0}'".format(id)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun vendedor con ese ID")
                else:
                    try:
                        consulta = "DELETE from vendedor where id_vendedor = {0}".format(id)
                        cur.execute(consulta)
                        filas = cur.fetchall()
                        print("VENDEDOR BORRADO CON EXITO")
                    except:
                        print("El vendedor no se puede borrar porque tiene ventas realizadas")
            if opcionSubmenu == 5:
                dni = str(input("Introduce DNI del vendedor que quieres borrar: "))
                consulta = "SELECT * from vendedor where DNI = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun vendedor con ese DNI")
                else:
                    try:
                        consulta = "DELETE from vendedor where dni = {0}".format(dni)
                        cur.execute(consulta)
                        filas = cur.fetchall()
                        print("VENDEDOR BORRADO CON EXITO")
                    except:
                        print("El vendedor no se puede borrar porque tiene ventas realizadas")
            submenu = "\n------------------------------\n"
            submenu +="    (1) Mostrar vendedores.\n"
            submenu +="    (2) Nuevo vendedor.\n"
            submenu +="    (3) Modificar vendedor.\n"
            submenu +="    (4) Borrar por ID.\n"
            submenu +="    (5) Borrar por DNI.\n"
            submenu +="        (0) Atrás\n\n    Elige una opción:"
            opcionSubmenu = int(input(submenu))
            print("\n------------------------------\n")
    if opcionMenuPrincipal == 4:
        opcionSubmenu = 6
        while opcionSubmenu != 0:
            if opcionSubmenu == 1:
                consulta = 'select *, (select nombre from categoria where id_categoria = fk_id_categoria) as categoria, (select empresa from proveedor where id_proveedor = fk_id_proveedor)as proveedor from producto'
                cur.execute(consulta)

                filas = cur.fetchall()

                for r in filas:
                    print('--->ID PRODUCTO: ', r[0], '\n     Nombre ', r[1],'\n     Descripción: ', r[2],"\n     Cantidad: ",r[3],"\n     Precio: ",r[4],"€\n     Altura: ",r[5],'cm\n     Anchura: ', r[6],'cm\n     Peso: ', r[7],'kg\n     Categoria: ', r[9],"\n     Proveedor: ",r[10])
            if opcionSubmenu == 2:
                nombre = str(input("Introduce nombre: "))
                descripcion = str(input("Introduce descripcion: "))
                cantidad = int(input("Introduce cantidad: "))
                precio = float(input("Introduce precio: "))
                altura = float(input("Introduce altura: "))
                anchura = float(input("Introduce anchura: "))
                peso = float(input("Introduce peso: "))
                nombreCAT = str(input("Introduce nombre de la categoria: "))
                proveedor = str(input("Introduce CIF del proveedor: "))
                consulta = "SELECT id_categoria from categoria where nombre = '{0}'".format(nombreCAT)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)!=0):
                    idCategoria = 0
                    for r in filas:
                        idCategoria = r[0]
                    consulta = "SELECT id_proveedor from proveedor where cif = '{0}'".format(proveedor)
                    cur.execute(consulta)
                    filas1 = cur.fetchall()
                    if (len(filas1)!=0):
                        idProveedor = 0
                        for r in filas1:
                            idProveedor = r[0]
                        consulta = "SELECT * from Producto where nombre = '{0}'".format(nombre)
                        cur.execute(consulta)
                        filas2 = cur.fetchall()
                        if (len(filas2)==0):
                            consulta = 'INSERT INTO producto (nombre, descripcion,cantidad,precio,altura,anchura,peso,fk_id_Categoria,fk_id_Proveedor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                            val = (nombre,descripcion,cantidad,precio,altura,anchura, peso, idCategoria, idProveedor)
                            cur.execute(consulta,val)
                            conn.commit()
                            print("PRODUCTO AÑADIDO CON EXITO")
                        else:
                            print("Ya existe un producto con ese nombre")
                    else:
                        print("No existe una proveedor con ese CIF")
                else:
                    print("No existe una categoria con ese nombre")
            if opcionSubmenu == 3:
                dni = str(input("Introduce nombre del producto al que vas a modificar los datos: "))
                consulta = "SELECT * from producto where nombre = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun producto con ese nombre")
                else:
                    modificar = str(input("¿Cambiar nombre?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = str(input("Introduce nuevo nombre: "))
                        consulta = 'UPDATE producto set nombre = %s where nombre=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                        dni = nombre
                    modificar = str(input("¿Cambiar descripcion?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = str(input("Introduce nueva descripcion: "))
                        consulta = 'UPDATE producto set descripcion = %s where nombre=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar cantidad?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = int(input("Introduce nueva cantidad: "))
                        consulta = 'UPDATE producto set cantidad = %s where nombre=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar precio?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = int(input("Introduce nuevo precio: "))
                        consulta = 'UPDATE producto set precio = %s where nombre=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar altura?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = int(input("Introduce nueva altura: "))
                        consulta = 'UPDATE producto set altura = %s where nombre=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar anchura?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = int(input("Introduce nueva anchura: "))
                        consulta = 'UPDATE producto set anchura = %s where nombre=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    modificar = str(input("¿Cambiar peso?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = int(input("Introduce nuevo peso: "))
                        consulta = 'UPDATE producto set peso = %s where nombre=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                        
                    print("PRODUCTO MODIFICADO CON EXITO")
            if opcionSubmenu == 4:
                id = str(input("Introduce id del producto que quieres borrar: "))
                consulta = "SELECT * from Producto where id_producto = {0}".format(id)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun producto con ese ID")
                else:
                    try:
                        consulta = "DELETE from producto where id_producto = {0}".format(id)
                        cur.execute(consulta)
                        print("PRODUCTO BORRADO CON EXITO")
                    except:
                        print("El producto no se puede borrar porque hay ventas con este producto.")
            if opcionSubmenu == 5:
                dni = str(input("Introduce nombre del producto que quieres borrar: "))
                consulta = "SELECT * from PRODUCTO where id_producto = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ningun producto con ese nombre")
                else:
                    try:
                        consulta = "DELETE from producto where nombre = '{0}'".format(dni)
                        cur.execute(consulta)
                        print("PRODUCTO BORRADO CON EXITO")
                    except:
                        print("El producto no se puede borrar porque hay ventas con este producto")
            submenu = "\n------------------------------\n"
            submenu +="    (1) Mostrar productos.\n"
            submenu +="    (2) Nuevo producto.\n"
            submenu +="    (3) Modificar producto.\n"
            submenu +="    (4) Borrar por ID.\n"
            submenu +="    (5) Borrar por nombre.\n"
            submenu +="        (0) Atrás\n\n    Elige una opción:"
            opcionSubmenu = int(input(submenu))
            print("\n------------------------------\n")
    if opcionMenuPrincipal == 5:
        opcionSubmenu = 6
        while opcionSubmenu != 0:
            if opcionSubmenu == 1:
                consulta = 'select *,(select nombre from vendedor where id_vendedor = (select fk_id_vendedor from cliente_vendedor_venta where fk_id_venta = id_venta))as vendedor,(select apellidos from vendedor where id_vendedor = (select fk_id_vendedor from cliente_vendedor_venta where fk_id_venta = id_venta))as vendedor2,(select nombre from cliente where id_cliente = (select fk_id_cliente from cliente_vendedor_venta where fk_id_venta = id_venta))as cliente,(select apellidos from cliente where id_cliente = (select fk_id_cliente from cliente_vendedor_venta where fk_id_venta = id_venta))as cliente2a,(select fecha from cliente_vendedor_venta where fk_id_venta = id_venta)as tiempo from venta'
                cur.execute(consulta)

                filas = cur.fetchall()

                for r in filas:
                    print('--->ID VENTA: ', r[0], '\n     Precio total ', r[1],'\n     Vendedor: ', r[2],r[3],"\n     Cliente: ", r[4],r[5],"\n     Fecha: ", r[6])
            if opcionSubmenu == 2:
                descripcion = str(input("Introduce DNI del vendedor: "))
                consulta = "SELECT * from vendedor where dni = '{0}'".format(descripcion)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)!=0):
                    idVendedor = 0
                    for r in filas:
                        idVendedor = r[0]
                    cliente = str(input("Introduce DNI del cliente: "))
                    consulta = "SELECT * from cliente where dni = '{0}'".format(cliente)
                    cur.execute(consulta)
                    filas1 = cur.fetchall()
                    if (len(filas1)!=0):
                        idCliente = 0
                        for r in filas1:
                            idCliente = r[0]
                        consulta = 'INSERT INTO venta (preciototal) VALUES (0);'
                        cur.execute(consulta)
                        conn.commit()
                        consulta = "SELECT * from venta"
                        cur.execute(consulta)
                        filas2 = cur.fetchall()
                        idVenta = 0
                        for r in filas2:
                            idVenta = r[0]
                        consulta = 'INSERT INTO cliente_vendedor_venta (fk_id_cliente, fk_id_vendedor,fk_id_venta) VALUES (%s,%s,%s);'
                        var = (idCliente,idVendedor,idVenta)
                        cur.execute(consulta,var)
                        productoOp = 10
                        precioTotal = 0.0
                        while productoOp != -1:
                            productoOp = int(input("Introduce id del producto a comprar(-1 para no añadir más): "))
                            if (productoOp!= -1):
                                consulta = "SELECT * from producto where id_producto = '{0}'".format(productoOp)
                                cur.execute(consulta)
                                filas5 = cur.fetchall()
                                if (len(filas5)!=0):
                                    for r in filas5:
                                        precioTotal += r[4]
                                    consulta = 'INSERT INTO venta_producto (fk_id_producto, fk_id_venta) VALUES (%s,%s);'
                                    var = (productoOp,idVenta)
                                    cur.execute(consulta,var)
                        consulta = 'UPDATE VENTA set preciototal = %s where id_venta=%s'
                        var = (precioTotal, idVenta)
                        cur.execute(consulta,var)
                        conn.commit()
                        print("VENTA AÑADIDA CON EXITO")
                    else:
                        print("No existe un cliente con ese DNI")
                else:
                    print("No existe un vendedor con ese DNI")
            if opcionSubmenu == 3:
                id = int(input("Introduce id de la venta que quieres borrar: "))
                consulta = "SELECT * from venta where id_venta = {0}".format(id)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ninguna venta con ese ID")
                else:
                    try:
                        consulta = "DELETE from venta_producto where fk_id_venta = {0}".format(id)
                        cur.execute(consulta)
                        consulta = "DELETE from cliente_vendedor_venta where fk_id_venta = {0}".format(id)
                        cur.execute(consulta)
                        consulta = "DELETE from venta where id_venta = {0}".format(id)
                        cur.execute(consulta)
                        conn.commit()
                        print("PRODUCTO BORRADO CON EXITO")
                    except:
                        print("El producto no se puede borrar porque hay ventas con este producto.")
            submenu = "\n------------------------------\n"
            submenu +="    (1) Mostrar ventas.\n"
            submenu +="    (2) Nueva venta.\n"
            submenu +="    (3) Borrar por ID.\n"
            submenu +="        (0) Atrás\n\n    Elige una opción:"
            opcionSubmenu = int(input(submenu))
            print("\n------------------------------\n")
    if opcionMenuPrincipal == 6:
        opcionSubmenu = 6
        while opcionSubmenu != 0:
            if opcionSubmenu == 1:
                consulta = 'select * from categoria;'
                cur.execute(consulta)

                filas = cur.fetchall()

                for r in filas:
                    print('--->ID CATEGORIA: ', r[0], '\n     Nombre ', r[1],'\n     DNI: ', r[2])
            if opcionSubmenu == 2:
                nombre = str(input("Introduce nombre: "))
                descripcion = str(input("Introduce descripción: "))
                consulta = "SELECT * from categoria where nombre = '{0}'".format(nombre)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    consulta = 'INSERT INTO Categoria (nombre, descripcion) VALUES (%s,%s);'
                    val = (nombre,descripcion)
                    cur.execute(consulta,val)
                    conn.commit()
                    print("CATEGORIA AÑADIDA CON EXITO")
                else:
                    print("Ya existe una categoria con ese nombre")
            if opcionSubmenu == 3:
                dni = str(input("Introduce el nombre de la categori al que vas a modificar los datos: "))
                consulta = "SELECT * from categoria where nombre = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ninguna categoria con ese nombre")
                else:
                    modificar = str(input("¿Cambiar nombre?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        nombre = str(input("Introduce nuevo nombre: "))
                        consulta = 'UPDATE categoria set nombre = %s where nombre=%s'
                        val = (nombre, dni)
                        cur.execute(consulta,val)
                        dni = nombre
                        conn.commit()
                    modificar = str(input("¿Cambiar descripcion?(ESCRIBIR SI PARA CAMBIAR): "))
                    if(modificar=='SI'):
                        apellidos = str(input("Introduce nueva descripcion: "))
                        consulta = 'UPDATE categoria set descripcion = %s where nombre=%s'
                        val = (apellidos, dni)
                        cur.execute(consulta,val)
                        conn.commit()
                    print("CATEGORIA MODIFICADO CON EXITO")
            if opcionSubmenu == 4:
                id = int(input("Introduce id de la categoria que quieres borrar: "))
                consulta = "SELECT * from categoria where id_categoria = {0}".format(id)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ninguna categoria con ese ID")
                else:
                    try:
                        consulta = "DELETE from categoria where id_categoria = {0}".format(id)
                        cur.execute(consulta)
                        conn.commit()
                        print("CATEGORIA BORRADA CON EXITO")
                    except:
                        print("La categoria no se puede borrar porque algunos productos pertenecen a esta")
            if opcionSubmenu == 5:
                dni = str(input("Introduce nombre de la categoria que quieres borrar: "))
                consulta = "SELECT * from categoria where nombre = '{0}'".format(dni)
                cur.execute(consulta)
                filas = cur.fetchall()
                if (len(filas)==0):
                    print("No existe ninguna categoria con ese DNI")
                else:
                    try:
                        consulta = "DELETE from categoria where nombre = '{0}'".format(dni)
                        cur.execute(consulta)
                        conn.commit()
                        print("CATEGORIA BORRADA CON EXITO")
                    except:
                        print("La categoria no se puede borrar porque algunos productos pertenecen a esta")
            submenu = "\n------------------------------\n"
            submenu +="    (1) Mostrar categorias.\n"
            submenu +="    (2) Nueva categoria.\n"
            submenu +="    (3) Modificar categoria.\n"
            submenu +="    (4) Borrar por ID.\n"
            submenu +="    (5) Borrar por NOMBRE.\n"
            submenu +="        (0) Atrás\n\n    Elige una opción:"
            opcionSubmenu = int(input(submenu))
            print("\n------------------------------\n")
    if opcionMenuPrincipal == 7:
        print()



    menu = "\n------------------------------\n"
    menu +="    (1) Clientes.\n"
    menu +="    (2) Proveedores.\n"
    menu +="    (3) Vendedores.\n"
    menu +="    (4) Productos.\n"
    menu +="    (5) Ventas.\n"
    menu +="    (6) Categorias.\n"
    menu +="        (0) Terminar\n\n    Elige una opción:"
    opcionMenuPrincipal = int(input(menu))
    print("\n------------------------------\n")


cur.close()
conn.close()