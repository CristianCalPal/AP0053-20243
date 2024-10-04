
class Calculadora:

  Pi=3.141592653589793238462643383279502
  e=2.7182818284590452353602874713527
  valor=0

  def __init__(self):
    pass

  def imprimirValor(self):
    print(self.valor)

  def sumar(self,*arg):
    contador=0
    for i in arg:
      contador=contador+float(i)
    self.valor=contador
    return contador

  def restar(self,*arg):
    contador=0
    for i in arg:
      contador=contador-float(i)
    self.valor=contador
    return contador

  def multiplicar(self,*arg):
    contador=0
    for i in arg:
      contador=contador*float(i)
    self.valor=contador
    return contador
  
  def dividir(self,*arg):
    contador=0
    for i in arg:
      contador=contador/float(i)
    self.valor=contador
    return contador

  def factorial(self,a):
    contador=1
    for number in range(1,a+1,1):
      contador=number*contador
    valor=contador
    return contador

  def cos(self,angulo):
    angulo= (angulo*angulo)**(1/2)
    while angulo>(2*float(self.Pi)):
      angulo=angulo-self.Pi
    coseno=1
    cuenta=1
    for fact in range(2,34,2):
      if cuenta%2==0:
        coseno+=(angulo**fact)/(self.factorial(fact))
      else:
        coseno-=(angulo**fact)/(self.factorial(fact))
      cuenta+=1
    valor=coseno
    return coseno


  def sen(self,angulo):
    angulo=(angulo*angulo)**(1/2)
    while angulo>(2*self.Pi):
      angulo=angulo-self.Pi

    seno=angulo
    cuenta=1
    for fact in range(3,33,2):
      if cuenta%2==0:
        seno+=(angulo**fact)/(self.factorial(fact))
      else:
        seno-=(angulo**fact)/(self.factorial(fact))
      cuenta+=1

    if angulo>0:
      self.valor=seno
      return seno
    else:
      self.valor=-seno
      return -seno

  def raizCuadrada(self,number):  # Lastimosamente esta serie solo funciona para numeros entre (-1,1), es una rara funcion que converge en un intervalo y despues diverge
    raiz=0
    for i in range(0,40,1):
      raiz+=((((-1)**i)*(self.factorial(2*i)))/((1-2*i)*(self.factorial(i)**2)*(4**i)))*((number+1)**i)
    return raiz

