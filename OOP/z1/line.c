#include "point.h"
struct line{
    point_t *start;
    point_t *end;
};
typedef struct line line_t;

void line_free(line_t *l)
{
    free(l);
}

struct point *line_get_start(line_t *l)
{
    return l->start;
}

struct point *line_get_end(line_t *l)
{
    return l->end;

}

double line_get_lenght(line_t *l)
{
    return 0;
}