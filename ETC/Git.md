# Git

## Git 사용 이유
* 협업
* 복구
* 백업

## Git 기본 명령어 (로컬 레포지토리)
1. `git init`
2. `git add {file.확장자}` or `git add .`
3. `git commit -m '커밋 내용(최대한 상세하게)'`
4. file 상태 :
   1. untracked
   2. tracked
5. git status : 현재 Local Repository 상태를 확인하는 명령어

## 협업과 복구 및 백업

### 원격 저장소 연결
1. github에 원격 저장소를 생성합니다.
2. 로컬 저장소(Repository)를 생성합니다.
3. 원격 저장소에 Push 하기 전에 반드시 최소 하나 이상의 Commit을 가져야한다.

### 연결 저장소 연결 명령어
1. git remote add origin {Repository URL}
2. git remote -v : origin  {Repository URL} : 등록한  Remote Repository 정보 확인
3. git push -u origin master : 로컬에서 생긴 커밋 내역을 업로드
   * git push
4. git pull origin master :  원격 저장소의 변화 사항을 업데이트
5. git clone {git Repository URL} : 원격 저장소를 복제 해온다 (원격 -> 로컬) 다운로드

## branch
master pointer 는 상용 branch

github는 병렬적인 작업이 가능. 이를 위해서 branch가 존재함.




























