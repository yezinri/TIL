# Git

> Git과 Github는 다르다!
> > Git은 분산 버전 관리 시스템
> > Github는 git을 통해 이용하는 cloud 서비스

## Git 사용 이유
* 협업
* 복구
* 백업

## Git 기본 명령어 (로컬 레포지토리)
1. Local Repository를 생성할 때 : `git init`
2. Working Directory에 생긴 변화 사항(파일 생성, 삭제, 수정 등...)을 버전으로 관리하고자, Staging Area에 올리는 명령어: `git add {file.확장자}`
   현재 경로를 의미하는 `git add .` : 현재 Working Directory에 생긴 모든 변경 사항을 한번에 Staging Area에 올리는 명령어
3. 버전을 기록할 때, Commit을 남길 때 : `git commit -m '커밋 내용(최대한 상세하게)'`
4. file 상태 :
   1. `untracked` : git이 아직 관리하고 있지 않다.(최초 생성 시)
   2. `tracked` : add 명령어를 통해서 Staging Area에 올라간 파일
5. git status : 현재 Local Repository의 상태를 확인하는 명령어 (습관처럼 입력해라!)

## 협업과 복구 및 백업
### 원격 저장소 연결
1. github에 원격 저장소를 생성합니다.
2. 로컬 저장소(Repository)를 생성합니다.
3. **원격 저장소에 Push 하기 전에 반드시 최소 하나 이상의 Commit을 가져야한다.**
   

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


