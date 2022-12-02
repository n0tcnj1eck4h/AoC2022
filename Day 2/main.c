#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>


enum ACTION {
  ROCK = 1, 
  PAPER,
  SCISSORS
};


static int beats(enum ACTION action, enum ACTION response) { 
  return ((action % 3) + 1) == response;
}

static int score(enum ACTION action, enum ACTION response) {
  if(action == response)      return 3 + response;
  if(beats(action, response)) return 6 + response;
  return response;
}

static enum ACTION parse(char in) {
  switch (in) {
    case 'A': case 'X': return ROCK;
    case 'B': case 'Y': return PAPER;
    case 'C': case 'Z': return SCISSORS;
  }

  printf("%c is not a valid action\n", in);
  assert(0);
}

static enum ACTION get_response(enum ACTION action, enum ACTION r) {
  int ret = ((action + r + 3) % 3) + 1;
  return ret ? ret : SCISSORS;
}

static const char* str(enum ACTION a) {
  static const char* strs[] = {
    "Rock    ",
    "Paper   ", 
    "Scissors"
  };

  return strs[a - 1];
}

int main() {
  enum ACTION action, response, response2;
  FILE* input;
  char a, r;

  input = fopen("input.txt", "r");

  if(!input) {
    printf("Failed to open input.txt");
    exit(1);
  }

  int total_score = 0;
  int total_score2 = 0;
  while(fscanf(input, "%c %c\n", &a, &r) != EOF) {
    action = parse(a);
    response = parse(r);
    response2 = get_response(action, response);

    total_score += score(action, response);
    total_score2 += score(action, response2);
    printf("%s \t%s \t%c \t%s \t%d \t%d\n", str(action), str(response), r,  str(response2), total_score, total_score2);
  }

  fclose(input);
  return 0;
}
