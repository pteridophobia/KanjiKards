#include <stdio.h>       // for printf()
#include <stdlib.h>      // for exit()
#include <string.h>      // for strcpy(), strcmp(), etc.
#include <libgen.h>      // for basename(), dirname()
#include <fcntl.h> 
#include <sys/stat.h>
#include <unistd.h>
#include <sys/types.h>
#include <dirent.h>
int myrcp(char *f1, char *f2)
{
    struct stat file1;
    struct stat file2;
    struct stat s1 = stat(f1, &file1);
    struct stat s2 = stat(f2, &file2);
    if (stat(f1, &s1) < 0)
    {
        printf("Exiting\n");
        exit(1);
    }
    else {
        if(( (S_ISREG(s1.st_mode))!= 0) && ((S_ISLNK(s1.st_mode)) != 0))
        {
            printf("reject f1\n");
            return;
        }
    }
    if(( (S_ISREG(s2.st_mode))!= -1) && (S_ISLNK(s2.st_mode) != -1))
    {
        printf("reject f2\n");
        return;
    }
    if (S_ISREG(s1.st_mode) == 0)
    {
         if ((stat(f1, &file1) < 0) || ((stat(f1, &file1) >= 0) && (IS_REG(s1.st_mode)== 0) ))
            return cpf2f(f1, f2);
	 else if ((stat(f1, &file1) >= 0) && (S_ISDIR(s1.st_mode)== 0))// f2 exist and is DIR
            return cpf2d(f1,f2);
    }
    if (S_ISDIR(s1.st_mode) == 0)
    {
        if (((S_ISREG(s2.st_mode)) >= 0) && (S_ISDIR(s2.st_mode) != -1))
        {
            printf("Reject \n");
            return;
        }
        else if ( stat(f2, &file2) < 0)
        {

            mkdir(f2, s1.st_mode)
        }
        else 
        {
            char buf[4098];
            strcpy(buf, f1);
            strcat(buf, "/");
            strcat(buf, f2);
            mkfir(buf, s1.st_mode);
            return cpd2d(f1, buf);////CHECK THIS
        }
        return cpf2d(f1,f2);
    }
}
int cpf2f(char *f1, char *f2)
{
    struct stat file1;
    struct stat file2;
    struct stat s1 = stat(f1, &file1);
    struct stat s2 = stat(f2, &file2);
    char buffer[4096];
    if(s1.st_ino == s2.st_ino)
    {
        printf("reject\n");
        return;
    }
    if((S_ISLNK(s1.st_mode)) && (s2 >= 0))
    {
        printf("reject\n");
        return;
    }
    if ((S_ISLINK(s1.st_mode) != -1) && (s2 < 0))
    {
        
        buffer[readlink(f1, buffer, 4098)] = '\0';
        symlink(buffer, f2);
        return;
    }
    int fdp1 = open(f1, O_RDONLY);
    int fdp2 = open(f2, O_WRONLY|O_CREAT|O_TRUNC, s1.st_mode);
    int length;
    while(length = read(fd2, buffer, 4096))
    {
        write(fd2, buffer, length);
    }
}
int cpf2d(char *f1, char *f2)
{
    char * bse = basename(f1);
    char * dir = dirname(f1);
    char dest[4098];
    strcpy(dest, f2);
    strcat(dest, "/");
    strcat(dest, bse);
    struct stat s2;
    int x = stat(dest, &s2);
    if ( x > 0)
    {
        cpf2f(f1, dest);
    }
    else
    {
        if (s_ISDIR(s2.st_mode))
        {
            cpf2d(f1, dest);
        }
        else
        {
            cpf2f(f1, dest);
        }
    }
}
int cpd2d(char *f1, char *f2)
{
    struct dirent * entry;
    DIR * directory;
    directory = opendir(f1);
    while (entry = readdir(directory))
    {
            struct stat s;
            stat(entry.d_name, &s);
            char path[4098];
            char path2[4098];
            strcpy(path, f1);
            strcat(path, "/");
            strcat(path, entry->d_name);
            strcpy(path2, f2);
            strcat(path2, "/");
            strcat(path2, entry->d_name);
            if (S_ISDIR(s.st_mode))
            {
                
                

            }
            else{

            }
    }    
}
int main(int argc, char *argv[])
{
  if (argc < 3){
     printf("usage: %d " myrcp(argv[1], arrgv[2]));
    return myrcp(argv[1], argv[2]);
  }
}