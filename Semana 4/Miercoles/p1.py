elementos = {
    "hidrogeno":{
        "numero": 1,
        "peso":1.0074,
        "simbolo": "H"
    },
    "helio":{
        "numero": 2,
        "peso":4.0074,
        "simbolo": "He"
    }   
}

print(elementos.get("hidrogeno").get("peso"))
print(elementos["hidrogeno"]["peso"])