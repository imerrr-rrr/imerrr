#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Alumno {
public:
string nombre;
float calificacion;

Alumno (string n, float c) {
nombre= n;
calificacion = c;
}
bool aprobado () {
return calificacion >=6;
}
};
int main() {
 vector <Alumno> alumnos;
alumnos.push_back(Alumno ("Ana",9));
alumnos.push_back(Alumno ("Luis",5));
alumnos.push_back(Alumno ("Sofia", 8));

for(int i=0; i < alumnos.size(); i++) {
cout<<alumnos[i].nombre<<" ";
cout<<alumnos[i].calificacion<<endl;
if (alumnos[i].aprobado())
cout<<"Aprobado"<<endl;
else
cout<<"Reprobado"<<endl;
}
return 1;
}
