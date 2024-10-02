#ifndef LINE_H_
#define LINE_H_
#include "point.h"

typedef struct line line_t;
line_t *line_new(struct point *p1,struct point *p2);
void line_free(line_t *l);
struct point *line_get_start(line_t *l);
struct point *line_get_end(line_t *l);
double line_get_lenght(line_t *l);
#endif