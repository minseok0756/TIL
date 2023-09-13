# git

## 버전 관리?

버전 관리 시스템은 파일 변화를 시간에 따라 기록했다가 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템이다. VCS(Version Control System 버전 관리 시스템)를 사용하면 각 파일을 이전 상태로 되돌릴 수 있고, 프로젝트를 통째로 이전 상태로 되돌릴 수 있고, 시간에 따라 수정 내용을 비교해 볼 수 있고, 누가 문제를 일으켰는지도 추적할 수 있고, 누가 언제 만들어낸 이슈인지도 알 수 있다. 

### 분산 버전 관리 시스템(DVCS)

Git, Mecurial, Bazaar, Darcs 같은 DVCS에서의 클라이언트는 단순히 파일의 마지막 스냅샷을 Checkout 하지 않는다. 그냥 저장소를 히스토리와 더불어 전부 복제한다. 서버에 문제가 생기면
이 복제물로 다시 작업을 시작할 수 있다. 클라이언트 중에서 아무거나 골라도 서버를 복원할 수 있다. Clone은 모든 데이터를 가진 진정한 백업이다.

게다가 대부분의 DVCS 환경에서는 리모트 저장소가 존재한다. 리모트 저장소가 많을 수도 있다. 그래서 사람들은 동시에 다양한 그룹과 다양한 방법으로 협업할 수 있다. 계층 모델 같은 중앙집중식 시스템으로는 할 수 없는 워크플로를 다양하게 사용할 수 있다.

## Git 기초

### 차이가 아니라 스냅샷

 Git은 데이터를 파일 시스템 스냅샷의 연속으로 취급하고 크기가 아주 작다. Git은 커밋하거나 프로젝트의 상태를 저장할 때마다 파일이 존재하는 그 순간을 중요하게 여긴다. 파일이 달라지지 않았으면 Git은 성능을 위해서 파일을 새로 저장하지 않는다. 단지 이전 상태의 파일에 대한 링크만 저장한다. Git은 데이터를 ***스냅샷의 스트림***처럼 취급한다.

### 거의 모든 명령을 로컬에서 실행

거의 모든 명령이 로컬 파일과 데이터만 사용하기 때문에 네트워크에 있는 다른 컴퓨터는 필요 없다. 대부분의 명령어가 네트워크의 속도에 영향을 받는 CVCS에 익숙하다면 Git이 매우 놀라울 것이다. 프로젝트의 모든 히스토리가 로컬 디스크에 있기 때문에 모든 명령이 순식간에 실행된다. 

예를 들어 Git은 프로젝트의 히스토리를 조회할 때 서버 없이 조회한다. 그냥 로컬 터베이스에서 히스토리를 읽어서 보여 준다. 그래서 눈 깜짝할 사이에 히스토리를 조회할 수 있다. 어떤 파일의 현재 버전과 한 달 전의 상태를 비교해보고 싶을 때도 Git은 그냥 한 달 전의 파일과 지금의 파일을 로컬에서 찾는다. 파일을 비교하기 위해 리모트에 있는 서버에 접근하고 나서 예전 버전을 가져올 필요가 없다. 즉 오프라인 상태이거나 VPN에 연결하지 못해도 막힘 없이 일 할 수 있다. 비행기나 기차 등에서 작업하고 네트워크에 접속하고 있지 않아도 커밋할 수 있다

### Git의 무결성

Git은 데이터를 저장하기 전에 항상 체크섬을 구하고 그 체크섬으로 데이터를 관리한다. 체크섬은 Git에서 사용하는 가장 기본적인(Atomic) 데이터 단위이자 Git의 기본 철학이다.

Git은 SHA-1 해시를 사용하여 체크섬을 만든다. 만든 체크섬은 40자 길이의 16진수 문자열이다. 파일의 내용이나 디렉토리 구조를 이용하여 체크섬을 구한다. SHA-1은 아래처럼 생겼다.
> 24b9da6552252987aa493b52f8696cd6d3b00373 <br>
Git은 모든 것을 해시로 식별한다. 실제로 Git은 파일을 이름으로 저장하지 않고 해당 파일의 해시로 저장한다.

### ***세 가지 상태***

Git은 파일을 Committed, Modified, Staged 이렇게 세 가지 상태로 관리한다.
- Committed란 데이터가 로컬 데이터베이스에 안전하게 저장됐다는 것을 의미한다.
- Modified는 수정한 파일을 아직 로컬 데이터베이스에 커밋하지 않은 것을 말한다.
- Staged란 현재 수정한 파일을 곧 커밋할 것이라고 표시한 상태를 의미한다.

이 세 가지 상태는 Git 프로젝트의 세 가지 단계와 연결돼 있다. Git 디렉토리, 워킹 트리, Staging Area 이렇게 세 가지 단계를 이해하고 넘어가자.
- Git 디렉토리는 Git이 프로젝트의 메타데이터와 객체 데이터베이스를 저장하는 곳을 말한다. 이 Git 디렉토리가 Git의 핵심이다. 다른 컴퓨터에 있는 저장소를 Clone 할 때 Git 디렉토리가 만들어진다.
- 워킹 트리는 프로젝트의 특정 버전을 Checkout 한 것이다. Git 디렉토리는 지금 작업하는 디스크에 있고 그 디렉토리 안에 압축된 데이터베이스에서 파일을 가져와서 워킹 트리를 만든다.
- Staging Area는 Git 디렉토리에 있다. 단순한 파일이고 곧 커밋할 파일에 대한 정보를 저장한다. Git에서는 기술용어로는 “Index” 라고 하지만, “Staging Area” 라는 용어를 써도 상관 없다.

Git으로 하는 일은 기본적으로 아래와 같다.
1. 워킹 트리에서 파일을 수정한다.
2. Staging Area에 파일을 Stage 해서 커밋할 스냅샷을 만든다. 모든 파일을 추가할 수도 있고 선택하여 추가할 수도 있다.
3. Staging Area에 있는 파일들을 커밋해서 Git 디렉토리에 영구적인 스냅샷으로 저장한다.

Git 디렉토리에 있는 파일들은 Committed 상태이다. 파일을 수정하고 Staging Area에 추가했다면 Staged이다. 그리고 Checkout 하고 나서 수정했지만, 아직 Staging Area에 추가하지 않았으면 Modified이다.

## CLI

Git을 사용하는 방법은 많다. CLI로 사용할 수도 있고 GUI를 사용할 수도 있다. 이 책에서는 Git CLI 사용법을 설명한다. Git의 모든 기능을 지원하는 것은 CLI 뿐이다.

## Git 설치 (Git 2.0.0 버전 기준)

### Windows에 설치

Windows에 Git을 설치하는 방법은 여러 가지다. 공식 배포판은 Git 웹사이트에서 내려받을 수 있다. http://git-scm.com/download/win에 가면 자동으로 다운로드가 시작된다. 

자동화된 설치 방식은 Git Chocolatey 패키지를 통해 이용해볼 수 있다. 패키지는 커뮤니티에 의해 운영되는 프로그램인 점을 알려드린다.

Windows에서도 Git을 사용하는 또 다른 방법으로 'GitHub Desktop’을 설치하는 방법이 있다. 이 인스톨러는 CLI와 GUI를 모두 설치해준다. 설치하면 Git을 Powershell에서 사용할 수 있다. 인증정보(Credential) 캐싱과 CRLF 설정까지 잘 된다. 이런 것들은 차차 배우게 될 것인데, Git 사용자라면 쓰게 될 기능들이다. 'GitHub Desktop’은 GitHub Desktop 웹사이트에서 내려받는다

## Git 최초 설정

`'git config’`라는 도구로 설정 내용을 확인하고 변경할 수 있다. Git은 이 설정에 따라 동작한다. 이때 사용하는 설정 파일은 세 가지나 된다.
1. `/etc/gitconfig `파일: 시스템의 모든 사용자와 모든 저장소에 적용되는 설정이다. `git config --system `옵션으로 이 파일을 읽고 쓸 수 있다. (이 파일은 시스템 전체 설정파일이기 때문에 수정하려면 시스템의 관리자 권한이 필요하다.)
2. `~/.gitconfig, ~/.config/git/config` 파일: 특정 사용자(즉 현재 사용자)에게만 적용되는 설정이다. `git config --global` 옵션으로 이 파일을 읽고 쓸 수 있다. 특정 사용자의 모든 저장소 설정에 적용된다.
3. `.git/config` : 이 파일은 Git 디렉토리에 있고 특정 저장소(혹은 현재 작업 중인 프로젝트)에만 적용된다. `--local` 옵션을 사용하면 이 파일을 사용하도록 지정할 수 있다. 하지만 기본적으로 이 옵션이 적용되어 있다. (당연히, 이 옵션을 적용하려면 Git 저장소인 디렉토리로 이동 한 후 적용할 수 있다.)

각 설정은 역순으로 우선시 된다. 그래서 `.git/config` 가 `/etc/gitconfig` 보다 우선한다.

Windows에서는 $HOME 디렉토리에서 `.gitconfig` 파일을 찾는다(C:\Users\$USER 디렉토리에서 찾음).
Windows에서 `/etc/gitconfig` 파일은 Windows Vista 이후 버전에서 `C:\ProgramData\Git\config` 에서 찾을 수 있다(C:\Program Files\Git\etc에서 찾을 수 있었음). 이 시스템 설정 파일의 경로는 `git config -f <file>` 명령으로 변경할 수 있다. 관리자 권한이 필요하다.

### 사용자 정보

Git을 설치하고 나서 가장 먼저 해야 하는 것은 사용자이름과 이메일 주소를 설정하는 것이다. Git은 커밋할 때마다 이 정보를 사용한다. 한 번 커밋한 후에는 정보를 변경할 수 없다.
```
$ git config --global user.name "John Doe" <br>
$ git config --global user.email johndoe@example.com
```
다시 말하자면 --global 옵션으로 설정하는 것은 딱 한 번만 하면 된다. 해당 시스템에서 해당 사용자가 사용할 때는 이 정보를 사용한다. 만약 프로젝트마다 다른 이름과 이메일 주소를 사용하고 싶으면 --global 옵션을 빼고 명령을 실행한다.

### 설정 확인

`git config --list` 명령을 실행하면 설정한 모든 것을 보여주어 바로 확인할 수 있다.

Git은 같은 키를 여러 파일(`/etc/gitconfig` 와 `~/.gitconfig` 같은)에서 읽기 때문에 같은 키가 여러 개 있을 수도 있다. 그러면 Git은 나중 값을 사용한다.

`git config <key>`(key는 `git config --list`에서 출력되는 key=value의 key를 의미) 명령으로 Git이 특정 Key에 대해 어떤 값을 사용하는지 확인할 수 있다.

Git이 설정된 값을 읽을 때 여러 파일에서 동일한 키에 대해 다른 값을 설정하고 있을 수 있다. 값이 기대한 값과 다를 수 있는데 값만 보고 쉽게 그 원인을 찾을 수 없다. 이 때 키에 설정된 값이 어디에서 설정되었는지 확인할 수 있는데 다음과 같은 명령으로 어떤 파일로부터 설정된 값인지를 확인할 수 있다. `git config --show-origin <key>`

## 도움말 보기

명령어에 대한 도움말이 필요할 때 도움말을 보는 방법은 두 가지로 동일한 결과를 볼 수 있다.
```
$ git help <verb>
$ man git-<verb>
```
예를 들면 `$ git help config`를 실행하면 `git config` 명령에 대한 도움말을 볼 수 있다.

Git 명령을 사용하기 위해 매우 자세한 도움말 전체를 볼 필요 없이 각 명령에서 사용할 수 있는 옵션들에 대해서 간략히 살펴볼수도 있다. `-h`, `--help` 옵션을 사용하면 Git 명령에서 사용할 수 있는 옵션들에 대한 간단한 도움말을 출력한다. `$ git add -h`을 실행하면 `git add`에서 사용할 수 있는 옵션들에 대해 살펴볼 수 있다.

## Git의 기초

### Git 저장소 만들기

주로 다음 두 가지 중 한 가지 방법으로 Git 저장소를 쓰기 시작한다.
1. 아직 버전관리를 하지 않는 로컬 디렉토리 하나를 선택해서 Git 저장소를 적용하는 방법
2. 다른 어딘가에서 Git 저장소를 Clone 하는 방법

#### 1. 기존 디렉토리를 Git 저장소로 만들기

프로젝트의 디렉토리로 이동한다. `$ cd /c/user/my_project`

`$ git init` 명령을 실행한다. 이 명령은 .git 이라는 하위 디렉토리를 만든다. .git 디렉토리에는 저장소에 필요한 뼈대 파일(Skeleton)이 들어 있다.

Git이 파일을 관리하게 하려면 `git add` 명령으로 파일을 추가하고 `git commit` 명령으로 커밋한다.

#### 2. 기존 저장소를 Clone 하기

다른 프로젝트에 참여하려거나(Contribute) Git 저장소를 복사하고 싶을 때 `git clone` 명령을 사용한다. Git은 서버에 있는 거의 모든 데이터를 복사한다. `git clone` 을 실행하면 프로젝트 히스토리를 전부 받아온다.

`git clone <url> <폴더명>` 명령으로 저장소를 Clone 한다.
```
$ git clone https://github.com/libgit2/libgit2 mylibgit
```
이 명령은 "mylibgit" 라는 디렉토리를 만들고 그 안에 .git 디렉토리를 만든다. 그리고 저장소의 데이터를 모두 가져와서 자동으로 가장 최신 버전을 Checkout 해 놓는다.<br>
`<폴더명>`을 사용하지 않으면 “libgit2”로 생성된다.

### 수정하고 저장소에 저장하기

워킹 디렉토리
- Tracked(관리대상임): 이미 스냅샷에 포함되어 있던 파일, 처음 저장소를 Clone 하면 모든 파일은 Tracked이면서 Unmodified 상태이다.
    - Unmodified(수정하지 않음)
    - Modified(수정함): 마지막 커밋 이후 처음으로 수정된 파일(파일마다 적용)
    - Staged(커밋으로 저장소에 기록할)
    - Modified -> Staged -> Committed를 반복한다.
- Untracked(관리대상이 아님): Tracked가 아닌 파일, 스냅샷에도 Staging Area에도 포함되지 않은 파일

#### 파일의 상태 확인하기

`git status` 명령을 사용한다. Clone한 후에 바로 이 명령을 실행하면 아래과 같은 메시지를 볼 수 있다.
```
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean
```
파일을 하나도 수정하지 않았다는 것을 말해준다. Tracked 파일은 하나도 수정되지 않았다는 의미다.

새로운 파일(README(Untracked files))을 만든다. `git status` 를 실행한다.
```
$ echo 'My Project' > README
$ git status
...
Untracked files:
  (use "git add <file>..." to include in what will be committed)
  README
nothing added to commit but untracked files present (use "git add" to
track)
```
README 파일이 Untracked 상태라는 것을 확인할 수 있다. Git은 Untracked 파일을 아직 스냅샷(커밋)에 넣어지지 않은 파일이라고 본다. 파일이 Tracked 상태가 되기 전까지는 Git은 절대 그 파일을 커밋하지 않는다.

#### 파일을 새로 추적하기

`git add` 명령으로 파일을 새로 추적할 수 있다.
```
$ git add README
```

`git status` 명령을 다시 실행한다.
```
$ git status
...
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
  new file: README
```
“Changes to be committed” 에 들어 있는 파일은 Staged 상태라는 것을 의미한다. 커밋하면 `git add` 를 실행한 시점의 파일이 커밋되어 저장소 히스토리에 남는다. `git add` 명령은 파일
또는 디렉토리의 경로를 아규먼트로 받는다. 디렉토리면 아래에 있는 모든 파일들까지 재귀적으로 추가한다.

#### Modified 상태의 파일을 Stage 하기

파일(CONTRIBUTING.md)을 수정하고 나서(Modified) `git status` 명령을 실행한다.
```
$ git status
...
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working
directory)
  modified: CONTRIBUTING.md
```
CONTRIBUTING.md파일이 modified 상태인 것을 확인할 수 있다. 

`git add` 명령은 파일을 새로 추적할 때도 사용하고 수정한 파일을 Staged 상태로 만들 때도 사용한다. Merge 할 때 충돌난 상태의 파일을 Resolve 상태로 만들때도 사용한다. add의 의미는 다음 커밋에 추가한다고 받아들이는게 좋다. `git add` 명령을 실행고 git status 명령을 실행한다.
```
$ git add CONTRIBUTING.md
$ git status
...
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
  new file: README
  modified: CONTRIBUTING.md
```
두 파일 모두 Staged 상태임을 확인할 수 있다. 

바로 커밋하지 않고 CONTRIBUTING.md 파일을 열고 수정한다. `git status` 명령으로 파일의 상태를 다시 확인해보자.
```
$ vim CONTRIBUTING.md
$ git status
...
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
  new file: README
  modified: CONTRIBUTING.md
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working
directory)
  modified: CONTRIBUTING.md
```
CONTRIBUTING.md 가 Staged 상태이면서 동시에 Unstaged 상태로 나온다. `git add` 명령을 실행하면 Git은 파일을 바로 Staged 상태로 만든다. 커밋을 하면 `git commit` 명령을 실행하는 시점의 버전이 커밋되는 것이 아니라 마지막으로 `git add` 명령을 실행했을 때의 버전이 커밋된다. 때문에 CONTRIBUTING.md가 staged이면서 Unstaged일 수 있는 것이다.