# Git记录的是什么？
# SVN记录的事每一次版本变动的内容
# Git则是将每个版本独立保存

# Git维护 工作区域 暂存区域 Git仓库 来实现版本控制

# gIt init
# 先要在工作的文件夹中初始化Git

# Git的工作流程一般是
#   1.在工作目录中添加修改文件
#   2.将需要进行版本管理的文件放入暂存区域
#   3.将暂存区域的文件提交到Git仓库

# Git管理的文件有三种状态：
#   -已修改（modified）
#   -已暂存（staged）
#   -已提交（committed）

# 提交文件：
# git add 文件名       ------add就是将文件添加到暂存区
# git add -A          ------可以提交工作区中所有的文件
# git commit -m "提交说明：你干了啥"  ------commit将暂存区文件提交到Git仓库

# 查看状态
# git status

# git restore 将暂存区域的文件恢复到工作区域，会丢失掉现在工作区的文件！！！

# 查看历史提交
# git log

#                   -add->            -commit->
# WorkingDirectory ------ Stage(Index) ------ Repository(HEAD)
#                 <-restore-          <-reset-

# git reset HEAD~
# 其中HEAD~表示回滚到上个版本的快照 如果两个~~就表示回滚到上上个版本的快照
# 或写作git reset HEAD~2表示回滚到上上版本

# git reset --mixed HEAD~
# --mixed参数表示
# 1.移动HEAD的指向，将其指向上一个快照
# 2.将HEAD移动后指向的快照回滚到暂存区域

# git reset --soft HEAD~
# --soft参数表示 移动HEAD的指向将其指向上一个快照，并不会修改暂存区
# 也就相当于撤回上一次的提交

# git reset --hard HEAD~
# --hard参数表示
# 1.移动HEAD的指向，将其指向上一个快照
# 2.将HEAD移动后指向的快照回滚到暂存区域
# 3.将暂存区域的文件还原到工作目录  （会覆盖掉工作目录里最新的文件！！！）

# 回滚指定快照
# git reset 至少6位的版本快照号

# 回滚个别文件
# git reset 版本快照 文件名/路径

# reset指令不仅可以回滚还可以往前滚（要记得版本号）
# git reflog 可以查看之前操作的日志

# 比较暂存区域和工作目录
# git diff

# 这里是不同

# 移动命令
# J向下移一行 K向上移一行
# F向下移一页 B向上移一页
# D向下移半页 U向上移半页

# 跳转命令
# g跳到第一行
# G跳到最后一行
# num g 跳到第num行
# num G 跳到倒数第num行

# 搜索命令
# / +关键词 从上往下搜索关键词
# ? +关键词 从下往上搜索关键词
# n 跳转到下一个搜索结果

# h 帮助文档

# q 退出

# 比较两个历史快照
# git diff 快照ID1 快照ID2

# 比较当前工作目录和GIt仓库中的快照
# git diff 快照ID
# 比较最新的一份快照和当前工作目录
# git diff HEAD

# 比较暂存区域和Git仓库快照
# git diff --cached 快照ID

# 修改最后一次提交
# 执行带 --amend选项的commit提交命令Git就会更正最近的一次提交
# git commit --amend
# 如果不希望修改:q!退出后包保留旧的说明
# 提交命令加上-m就不进入提交说明的界面

# 删除文件
# git rm 文件名
# 删除工作目录和暂存区域的文件
# 也就是取消跟踪，在下次提交时不纳入版本管理
# 不会删除在仓库快照里的文件 如果要删除要移除掉快照
# 如果你工作区和暂存区有两个不同的文件 会不知道你删除哪个
# 使用-f  指令强制删除工作区和暂存区文件
# 使用--cached 文件名  只删除暂存区的文件

# 重命名文件
# git mv 旧文件名 新文件名


# 其他版本控制系统的分支
# 克隆一份全新的目录以同样拥有5个分支来说，SVN是同事复制5个版本的文件，
# 也就是说重复5次同样的动作。而Git只是获取文件的每个版本的元素，
# 然后只载入主要的分支(master)
# 克隆一份已拥有近1W个commit,5个分支,每个分支大约有1500个文件的SVN需要将近1小时
# 而Git只用了1分钟

# 创建分支
# git branch 分支名

# 查看指向提交的所有引用比如分支或者标签
# git log --decorate
# --oneline 参数一行显示一个快照（log精简版）

# 切换分支
# git checkout 分支名

# 创建并切换到分支中
# git checkout -b 分支名

# 图形化显示各快照
# git log --decorate --oneline --graph --all
# --graph 图形化显示
# --all   显示所有快照

# Git工作流程

# 开发分支（develop）
# 代替单一的master主分支，可以使用两个分支来处理项目发布和日常开发
# master主分支通常只是用于对外发布项目的新版本，日常开发应该在另一条分支上完成
# 我们把开发用的分支叫develop分支

# 功能分支（feature）
# 每一个新功能应该使用单独一个功能分支进行开发，功能分支应该从开发分支中分离出来
# 功能开发完成后合并到开发分支
# 注意:
# 1.功能分支不应该跟master分支有任何交流
# 2.功能分支可以采用feature-新功能名的形式命名

# 预发布分支（release）
# 在项目正式发布之前，可能与要一个预发布的版本进行测试，于是你可以从开发分支中分离
# 出预发布分支,用于内部或公开的测试
# 注意:
# 1.预发布分支应该同时合并到主分支和开发分支中
# 2.预发布分支可以采用release-版本的形式命名

# 维护分支(hotfix)
# 项目正式发布后难免会出现bug，这是就需要创建一个分支，进行bug的修补
# 注意：
# 1.维护分支应该从主分支中分离出来，bug被修补后，再河滨道主分支和开发分支中
# 2.维护分支可以采用fixbug-*的形式命名

# 常设分支
# 常设分支就主分支（master）和开发者分支（develop）两个即可，另外的功能分支、
# 维护分支、预发布分支属于临时分支，用完应该及时删除。

# 分支合并
# git merge 分支名
# 将指定分支合并到本分支

# 删除分支
# git branch -d 分支名
# 删除分支后名字丢失了其实快照还在，因为分支实际上就是一个指针指向一个快照
