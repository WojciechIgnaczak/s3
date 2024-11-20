#include <iostream>
using namespace std;

class Media{
    public:
    Media(const string& _file_name): file_name(_file_name){};
    virtual void play()const=0;
    virtual void pause()const=0;
    const string& getFilename() const{return file_name;}
    virtual ~Media(){};
    private:
    string file_name;
};

class AudioPlayer: virtual public Media{
    public:
    AudioPlayer (const string& _file_name): Media(_file_name){};
    void setVolume(int _volume){volume=_volume;}
    virtual void play()const override{
        cout<<"AudioPlayer: playing: "<<getFilename()<<endl;
    }
    virtual void pause()const override{
        cout<<"AudioPlayer: paused: "<<getFilename()<<endl;
    }

    private:
    int volume;
};

class VideoPlayer: virtual public Media{
    public:
    VideoPlayer(const string& _file_name): Media(_file_name){};
    void setBrightness(int _brightness){brightness=_brightness;}
    virtual void play()const override{
        cout<<"VideoPlayer: playing: "<<getFilename()<<endl;
    }
    virtual void pause()const override{
        cout<<"VideoPlayer: paused: "<<getFilename()<<endl;
    }
    private:
    int brightness;
};

class AVPlayer: public AudioPlayer, public VideoPlayer{
public:
    AVPlayer(const string& _file_name): Media(_file_name),VideoPlayer(_file_name),AudioPlayer(_file_name){};
    void play()const{
        cout<<"AVPlayer: synchronizing a/v: "<<getFilename()<<endl;
        AudioPlayer::play();
        VideoPlayer::play();
    }
    void pause()const{
        cout<<"AVPlayer: pausing: "<<getFilename()<<"\n";
        AudioPlayer::pause();
        VideoPlayer::pause();
    }
};

int main(){
    AVPlayer p("plik_audio_video.txt");
    p.play();
    p.pause();
    
    return 0;
}