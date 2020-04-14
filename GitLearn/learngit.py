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
