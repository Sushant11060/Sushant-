#include<stdio.h>
#include<math.h>

int main()
{

    int x1, y1, x2, y2, x3, y3, x4, y4;

    printf("Enter coordinates of point 1 : ");
    scanf("%d %d", &x1, &y1);
    printf("Enter coordinates of point 2 : ");
    scanf("%d %d", &x2, &y2);
    printf("Enter coordinates of point 3 : ");
    scanf("%d %d", &x3, &y3);
    printf("Enter coordinates of point 4 : ");
    scanf("%d %d", &x4, &y4);

    // side of rectangle 
    int d1 = pow((x2 - x1),2) + pow((y2 - y1),2);
    int d2 = pow((x3 - x2),2) + pow((y3 - y2),2);
    int d3 = pow((x4 - x3),2) + pow((y4 - y3),2);
    int d4 = pow((x1 - x4),2) + pow((y1 - y4),2);

    // diagonals
    int diag1 = pow((x3 - x1),2) + pow((y3 - y1),2);
    int diag2 = pow((x4 - x2),2) + pow((y4 - y2),2);

    // Check if opposite sides and diagonals are equal or not
    if (d1 == d3 && d2 == d4 && diag1 == diag2)
        {printf("The points form a rectangle.\n");}
    else
        {printf("The points do not form a rectangle.\n");}

    return 0;
    
}
