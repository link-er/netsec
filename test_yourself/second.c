#include "data_05.h"
#include <stdio.h>

int main()
{
  register int i;
  unsigned int max = data[0], second_max = data[0], temp;

  for(i = 1 ; i < sizeof(data)/4; ++i) {
    if(data[i] > max) {
      temp = max;
      max = data[i];
      second_max = temp;
    }

    if(data[i] < max && data[i] > second_max) {
      second_max = data[i];
    }
  }

  printf("%u\n", second_max);

  return 0;
}
