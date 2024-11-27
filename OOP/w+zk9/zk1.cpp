#include <iostream>

template <typename T>
class Node {
public:
    Node(T value) : data(value), next(nullptr) {}
    T data;
    Node<T> *next;
};


template <typename T>
class Container{
public:
    virtual void push(const T &value)=0;
    virtual T pop()=0;
    virtual bool isEmpty() const=0;
    virtual size_t size() const=0;
    virtual ~Container(){};
};


template <typename T>
class Queue: public Container<T>{
public:    
    Queue():first(nullptr), last(nullptr), counter(0){};
    virtual void push(const T &value)override{

        Node<T> *newNode= new Node<T>(value);
        if(last)
        {
            last->next=newNode;
        }else{
            first=newNode;
        }
        last=newNode;
        ++counter;
    }
    virtual T pop()override
    {
        if(isEmpty())
        {throw std::out_of_range("Queue is empty");
        }
        Node<T> *temp= first;
        T value_first=temp->data;
        first=first->next;
        if(!first)
        {
            last=nullptr;
        }
        delete temp;

        counter--;
        return value_first;
    }
    virtual bool isEmpty() const override{
        if(counter==0){
            return true;
        }else{return false;}
    }
    virtual size_t size() const override{
        return counter;
    }
private:
    Node<T>* first;
    Node<T>* last;
    size_t counter;
};


template <typename T>
class Stack: public Container<T>{
public:
    Stack():head(nullptr),counter(0){};
    virtual void push(const T &value)override{
        Node<T> *newNode= new Node<T>(value);
        newNode->next=head;
        head=newNode;
        ++counter;
    }
    
    virtual T pop()override
    {
        if(isEmpty()){throw std::out_of_range("Stack is empty");}
        Node<T> *newNode= head;
        T ret=newNode->data;
        head=newNode->next;
        delete newNode;
        counter--;
        return ret;
        
    }
    virtual bool isEmpty() const override{
        if(counter==0)
        {
            return true;
        }else{return false;}
    }
    virtual size_t size() const override{
        return counter;
    }
private:
Node<T>* head;
size_t counter;
};




int main()
{
    try{
        Queue<int> q;
        q.push(1);
        q.push(2);
        q.push(3);
        while(!q.isEmpty())
        {
            std::cout<<q.pop()<<std::endl;
        }
        Stack<int> s;
        s.push(1);
        s.push(2);
        s.push(3);
        while(!s.isEmpty())
        {
            std::cout<<s.pop()<<std::endl;
        }   
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }
    return 0;
}






