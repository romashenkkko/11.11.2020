n=int(input('numarul este '))
if (n>=28) and (n<=31):
    if n==28:
        print('februarie, an obisnuit')
    if n==29:
        print('februarie an bisect')
    if n==30:
        print('aprilie, iunie, septembrie, noiembrie')
    if n==31:
        print('ianuarie, martie, mai, iulie, octombrie, decembrie')
else:
    print('Eroare')