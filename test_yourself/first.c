#include <sys/types.h>
#include <stdio.h>

#define KEY 0x0f

int encrypt(u_char* buf, int len) {
  register int i;

  if (!buf) return 0;

  for (i = 0 ; i < len; ++i) {
    printf("%c %d\n", buf[i], i);

    buf[i] = (buf[i] ^ KEY) + i;
  }

  return i;
}

int decrypt(u_char* buf, int len) {
  register int i;

  if (!buf) return 0;

  for (i = 0 ; i < len; ++i) {
    printf("%c %d\n", buf[i], i);

    buf[i] = (buf[i] - i) ^ KEY;
  }

  return i;
}

int main()
{
  u_char word[7] = {'\\','a','e','|','n','p','4'};
  int result = decrypt(word, 7);
  printf("%d %s\n", result, word);

  return 0;
}
