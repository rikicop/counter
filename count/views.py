from django.shortcuts import render,redirect
from .models import Transaccion, Cincuenta, Cargo
import pandas as pd
import json

def home(request):
    #Validación de que no esté vacio el campo cuenta
    if request.method == "POST" and request.POST.get('cuenta')=='':
        nuevo="Debe ingresar cuenta!"
        items = list(Transaccion.objects.all().values())
        return render(request, 'home.html', {'nuevo':nuevo, 'elementos':items})

    if request.method == "POST" and request.POST.get('cuenta'):
        #trans=Transaccion()
        cue= request.POST.get('cuenta')
        nomb= request.POST.get('nombre')
        mov= request.POST.get('movimiento')
        niv= request.POST.get('nivel')
        moneda= request.POST.get('moneda')
        asi= request.POST.get('asiento')
        carg= request.POST.get('cargo')
        abo= request.POST.get('abono')
        coda= request.POST.get('codant')
        ofi= request.POST.get('oficina')
        ban= request.POST.get('banco')
        proy= request.POST.get('proyecto')

        #codigo compuesto
        codcomp= cue + nomb #prueba
        print("Dos en uno: ",codcomp)
   
        if Transaccion.objects.filter(cuenta=cue).exists():
            print("Si existo")
      
            #Esta linea de abajo es la encargada de actualizar el objeto en particular
            Transaccion.objects.filter(cuenta=cue).update(cuenta=cue,
                nombre=nomb, movimiento=mov,nivel=niv,moneda=moneda,asiento=asi,
                ctacargo=carg,ctaabono=abo,codant=coda,oficina=ofi,banco=ban,proyecto=proy
            )
            items = list(Transaccion.objects.filter(nombre=nomb).values())
            return render(request, 'home.html', {'elementos':items})
        else:
            #Esta linea de abajo es la encargada de crear un objeto en particular
            crear = Transaccion(cuenta=cue,
                nombre=nomb, movimiento=mov,nivel=niv,moneda=moneda,asiento=asi,
                ctacargo=carg,ctaabono=abo,codant=coda,oficina=ofi,banco=ban,proyecto=proy
            )
            crear.save()
            nuevo="Usted ha creado un nuevo objeto: "
            #Aqui estoy intentando que sea ordenado
            #items = list(Transaccion.objects.all().order_by('-cuenta').values())
            items = list(reversed(Transaccion.objects.all().values()))
            
            return render(request, 'home.html', {'nuevo':nuevo,'elementos':items,'cuenta':cue})

        #Quiero Esto|Esto de abajo solo va acorrer si le das al botón de guardar
        print("Este es buscado: ", nomb)
        items = list(Transaccion.objects.filter(nombre=nomb).values())
        print("Esta es la lista generada por buscado: ", items)

        return render(request, 'home.html', {'elementos':items})
        
        #items = Transaccion.objects.filter(cuenta='0123') Busca uno en particular
        
    #BUSCAR  
    if request.method == "POST" and request.POST.get('buscar'):
        #Este es el select
        busc = request.POST.get('buscar')
        y=request.POST.get('s_buscar')
        print('s_buscar: ',y) #si funciona
        if y == 'nombre':
            items = list(Transaccion.objects.filter(nombre=busc).values())
            print("Este es el resultado de la busqueda: ", items)
            return render(request, 'home.html', {'elementos':items})
        elif y == 'cuenta':
            items = list(Transaccion.objects.filter(cuenta=busc).values())
            print("Este es el resultado de la busqueda: ", items)
            return render(request, 'home.html', {'elementos':items})
    #BORRAR
    if request.method == "POST":
        if request.POST.get('bcuenta')=='':
            elimi="Debe ingresar cuenta a través del botón Edit!"
            items = list(Transaccion.objects.all().values())
            return render(request, 'home.html', {'elimi':elimi, 'elementos':items})

    if request.method == "POST":
         if request.POST.get('cuenta')!='':
            print("borrar")
            cue = request.POST.get('bcuenta')
            print(cue)
            Transaccion.objects.get(cuenta=cue).delete()
            items = list(Transaccion.objects.all().values())
            return render(request, 'home.html', { 'elementos':items})

       
    #POR DEFECTO SIMPRE CORRE LA TABLA    
    items = list(Transaccion.objects.all().order_by('cuenta').values())
    return render(request, 'home.html', {'elementos':items})


def cincuenta(request):
    if request.method == "POST" and request.POST.get('cuenta')=='':
        nuevo="Debe ingresar cuenta!"
        items = list(Cincuenta.objects.all().values())
        return render(request, 'home.html', {'nuevo':nuevo, 'elementos':items})

    if request.method == "POST" and request.POST.get('cuenta'):
  
        cue= request.POST.get('cuenta')
        nomb= request.POST.get('nombre')
        mov= request.POST.get('movimiento')
        niv= request.POST.get('nivel')
        moneda= request.POST.get('moneda')
        asi= request.POST.get('asiento')
        carg= request.POST.get('cargo')
        abo= request.POST.get('abono')
        coda= request.POST.get('codant')
        ofi= request.POST.get('oficina')
        ban= request.POST.get('banco')
        proy= request.POST.get('proyecto')

       
        codcomp= cue + nomb #prueba
        print("Dos en uno: ",codcomp)
   
        if Cincuenta.objects.filter(cuenta=cue).exists():
            print("Si existo")
      
           
            Cincuenta.objects.filter(cuenta=cue).update(cuenta=cue,
                nombre=nomb, movimiento=mov,nivel=niv,moneda=moneda,asiento=asi,
                ctacargo=carg,ctaabono=abo,codant=coda,oficina=ofi,banco=ban,proyecto=proy
            )
            items = list(Cincuenta.objects.filter(nombre=nomb).values())
            return render(request, 'home.html', {'elementos':items})
        else:
           
            crear = Cincuenta(cuenta=cue,
                nombre=nomb, movimiento=mov,nivel=niv,moneda=moneda,asiento=asi,
                ctacargo=carg,ctaabono=abo,codant=coda,oficina=ofi,banco=ban,proyecto=proy
            )
            crear.save()
            nuevo="Usted ha creado un nuevo objeto: "
            
            items = list(reversed(Cincuenta.objects.all().values()))
            
            return render(request, 'home.html', {'nuevo':nuevo,'elementos':items,'cuenta':cue})

        
        print("Este es buscado: ", nomb)
        items = list(Cincuenta.objects.filter(nombre=nomb).values())
        print("Esta es la lista generada por buscado: ", items)

        return render(request, 'home.html', {'elementos':items})
        
       
        
    #BUSCAR  
    if request.method == "POST" and request.POST.get('buscar'):
       
        busc = request.POST.get('buscar')
        y=request.POST.get('s_buscar')
        print('s_buscar: ',y) 
        if y == 'nombre':
            items = list(Cincuenta.objects.filter(nombre=busc).values())
            print("Este es el resultado de la busqueda: ", items)
            return render(request, 'home.html', {'elementos':items})
        elif y == 'cuenta':
            items = list(Cincuenta.objects.filter(cuenta=busc).values())
            print("Este es el resultado de la busqueda: ", items)
            return render(request, 'home.html', {'elementos':items})
    #BORRAR
    if request.method == "POST":
        if request.POST.get('bcuenta')=='':
            elimi="Debe ingresar cuenta a través del botón Edit!"
            items = list(Cincuenta.objects.all().values())
            return render(request, 'home.html', {'elimi':elimi, 'elementos':items})

    if request.method == "POST":
         if request.POST.get('cuenta')!='':
            print("borrar")
            cue = request.POST.get('bcuenta')
            print(cue)
            Cincuenta.objects.get(cuenta=cue).delete()
            items = list(Cincuenta.objects.all().values())
            return render(request, 'home.html', { 'elementos':items})

     
    items = list(Cincuenta.objects.all().order_by('cuenta').values())
    return render(request, 'home.html', {'elementos':items})

def tabla(request):
    #DF TO JSON
    df= pd.DataFrame(list(Cargo.objects.all().values()))

    print("Esta es la tabla Cargo: ", df)

    json_records = df.reset_index().to_json(orient ='records')
    dt_j = []
    dt_j = json.loads(json_records)
    
    #FIN DF TO JSON
    cargo = list(Cargo.objects.all().values())
    cincuenta = list(Cincuenta.objects.all().values())

    context = {'cargo':cargo,'cincuenta':cincuenta, "json1":dt_j, 'dt_j': dt_j} 
    return render(request, 'tabla.html', context)
    








     