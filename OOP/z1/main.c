#include <stdio.h>
#include "line.h"
#include "point.h"

int main()
{
    point_t *p1=point_new(10,20);
    point_t *p2=point_new(30,40);
    line_t *l1= line_new(p1,p2);

    printf("długosc liniii: %f\n",line_get_length(l1));
    line_free(l1);
    point_free(p2);
    point_free(p1);
}

point_t *point_new(int x, int y)
{
    point_t *p=malloc(sizeof(struct point));
    p->x=x;
    p->y=y;
    return p;
}

line_t *line_new(point_t *p1, point_t *p2)
{
    line_t *l=malloc(sizeof(struct line));
    l->start=p1;
    l->end=p2;
    return l;
}