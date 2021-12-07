#include <stdio.h>
#include <stdlib.h>

int main(){
  int numbers[5000],fuel[5000];
  int i = 0, j=0;
  FILE *file;

  if (file = fopen("input.txt", "r"))
  {
    while (fscanf(file, "%d,", &numbers[i]) != EOF)
    {
      i++;
    }
    fclose(file);
	}
	int k = 0,tot,l = 0,check;
	while (k < i){
		tot = 0;
		for(j = 0;j<i;j++){
			check = numbers[j] - k;
			if (check < 0) {check *= -1;}
			tot += check;
		}
		fuel[l] = tot;
		k++;
		l++; 
	}
	int min = fuel[0];
	for (j = 0;j<i;j++){
		if (min > fuel[j]){
			min = fuel[j];
		}
	}
	
	printf("%d",min);

    
	return 0;
}

