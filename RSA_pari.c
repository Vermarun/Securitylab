#include <pari/pari.h>
//#include<time.h>
GEN
extgcd(GEN A, GEN B, GEN *U, GEN *V)
{
  pari_sp av = avma;
  GEN ux = gen_1, vx = gen_0, a = A, b = B;

  if (typ(a) != t_INT) pari_err_TYPE("extgcd",a);
  if (typ(b) != t_INT) pari_err_TYPE("extgcd",b);
  if (signe(a) < 0) { a = negi(a); ux = negi(ux); }
  while (!gequal0(b))
  {
    GEN r, q = dvmdii(a, b, &r), v = vx;

    vx = subii(ux, mulii(q, vx));
    ux = v; a = b; b = r;
  }
  *U = ux;
  *V = diviiexact( subii(a, mulii(A,ux)), B );
  gerepileall(av, 3, &a, U, V); return a;
}
GEN encrpt(GEN msg,GEN e,GEN n){

	GEN Cipher;
	Cipher = Fp_pow(msg,e,n);
	return Cipher;
}
GEN decrpt (GEN C,GEN d,GEN n){
	
	GEN M;
	M = Fp_pow(C,d,n);
	return M;

	}
int main(){

	GEN n,p,q,phi_value,e,d,u,v,C;
	GEN msg;
//	char s = 'A';
	pari_init(1000000,2);
//	void setrand(time(null));
	printf("Enter the value:(greater than 2048)");p=gp_read_stream(stdin);
	printf("Enter the value"); q = gp_read_stream(stdin);
	printf("Enter the msg:");  msg = gp_read_stream(stdin);
//	x = (GEN) 1024;
//	msg = s;
	p = nextprime(randomi(p));
	q = nextprime(randomi(q));

	n = gmul(p,q);
	phi_value = gmul(gsubgs(p,1),gsubgs(q,1));

	e = randomi(phi_value);
	while(!gequal1(gcdii(e,phi_value))){
		e = randomi(phi_value);
	}
	extgcd(e,phi_value,&u,&v);
	d = u;
	C = encrpt(msg,e,n);
	pari_printf("d=%Ps\n",d);	
	pari_printf("Cipher=%Ps\n",C);
	pari_printf("Msg = %Ps\n",decrpt(C,d,n));
	pari_close();
return 0;
}
