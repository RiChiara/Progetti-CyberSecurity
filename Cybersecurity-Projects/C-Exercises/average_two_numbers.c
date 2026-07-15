/*
Si scriva un programma in linguaggio C 
che legga due valori interi 
e visualizzi la loro media aritmetica.
*/


# include <stdio.h>
int main ()
{
    int primo_valore;
    int secondo_valore;
    int risultato;
    
    printf("Leggimi il primo valore:  ");
    scanf("%d", &primo_valore);

    printf("\nLeggimi il secondo valore: ");
    scanf("%d",&secondo_valore );
    
    printf("\nQuesta è la media tra i due numeri: ");
    risultato=(primo_valore + secondo_valore)/2;
     printf("%d", risultato);
 return 0;
}
    