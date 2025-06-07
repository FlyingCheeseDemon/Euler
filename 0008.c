#include <stdio.h>

long array_product(int numbers[]);

void shift_array(int numbers[], int number);

int main() {
    FILE *fptr;
    // Open a file in read mode
    fptr = fopen("0008.txt", "rt"); 

    long largest_product = 0;
    long product = 0;
    int number_subset[13];

    int i=0;
    int currentChar;
    int numvalue;
    // Read the content and print it
    while((currentChar = fgetc(fptr)) != EOF) {
        numvalue = currentChar - 48;
        if (numvalue >= 0) {
            if(i < 12){
                number_subset[i] = numvalue;
            }else if (i == 12){
                number_subset[i] = numvalue;
                largest_product = array_product(number_subset);
            }else{
                shift_array(number_subset,numvalue);
                product = array_product(number_subset);
                if (product > largest_product){
                    largest_product = product;
                }
            }
            i++;
        }
    }

    printf("%li\n",largest_product);
    
    fclose(fptr); 
    return 0;
} 

long array_product(int numbers[]) {
    long product = numbers[0];
    for(int j = 1;j < 13;j++) {
        product = product*numbers[j];
    }
    return product;
}

void shift_array(int numbers[], int number) {
    int j;
    for(j = 0;j < 12;j++){
        numbers[j] = numbers[j+1];
    }
    numbers[12] = number;
}