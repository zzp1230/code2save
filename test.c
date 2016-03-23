#include "utf8_utils.h"
#include "ic_mem.h"
#include "err/errdo.h"

int main(int argc, char *argv[])
{
    
    char *flag=NULL;
    char *splittag=" ";
    clock_t start;
    char *minWs=(char*)malloc(sizeof(char)*128000000);
    int n,nn;
    while(1){
        
        
        flag=fgets(minWs,128000000,stdin);
        if((flag==NULL)||(feof(stdin))||(ferror(stdin))){ break;}
        
        if (minWs[strlen(minWs)-1]=='\n') {
            minWs[strlen(minWs)-1] = '\0';
        }
        if (strcmp(minWs,"quit")==0) {
            break;
        }
        char *wordLIST[5000];
        nn=0;
        char *content=(char*)malloc(sizeof(char)*20000);
        //-----去除特殊符号－－－－
        struct ic_mem_list *world_list=utf8_char_list(minWs);
        
        struct ic_mem_list_node* cup=world_list->head;
        int tag_first=0;
        for (n=0; n<world_list->size; n++) {
            if (tag_first==0) {
                
                strcpy(content,cup->key);
                nn+=1;
                tag_first+=1;
            }else
            {
                strcat(content,splittag);
                strcat(content,cup->key);
                nn+=1;
                
            }
            cup=cup->next;
        }
        ic_mem_list_free(world_list);
        //-----去除特殊符号－－－－
        
        printf("%s\n",content);
        
        free(content);
        for (n=0; n<nn; n++) {
            free(wordLIST[n]);
        }
        
    }//while结束
    free(minWs);
}
