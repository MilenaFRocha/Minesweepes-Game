#include <stdio.h>
#include <stdlib.h>


    int verificar_impar (int numero);
        int numero;

            for(int i =1 ;i <= sqrt(numero); i++){
                if (numero % i == 0){
                    printf("nao é primo\n");
                }else{
                    printf("é primo\n");
                }
        }

int main (void){

    int numero ;
    scanf("%d", &numero);

    resultado = verificar_impar(numero);
    printf("%d", resultado);


return 0;
}