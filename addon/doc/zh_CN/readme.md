# NVDA 插件实用程序手册

这个插件试图成为安装和卸载插件的实用程序包。

尝试为批量操作插件提供可能性，而不必像在插件管理器中那样一个接一个地进行。

随着新功能的添加，已添加的区域将在不同版本中得到改进。

此插件可以从 NVDA 菜单 ➡ 工具 ➡ NVDA 插件实用程序启动。

该插件没有分配用于快速启动的热键。

可在选项 ➡ 按键与手势菜单中添加一个快捷键，在类别中查找NVDA 插件实用程序。


## 免责声明

用户对插件的使用负最终责任。

我们试图使一切尽可能可靠，但问题总是会出现，因此插件作者将不对因使用此插件而引起的任何问题负责。

# 概述

该插件由 3 个部分组成。

* 第 1 部分：列出可以在其中选择要使用的类别的列表。这是每次调用插件时焦点所在的地方。

在该列表中可使用上、下箭头进行移动。

* 第二部分：包含所选类别内容的区域。

此区域将根据类别而变化。类别说明请见下文。

可以使用键盘快捷键或 Tab 键从类别中访问。

* 第三部分：此部分包含一个编辑框，当执行操作时将激活该编辑框，向用户提供正在操作的信息。用户还将收到有关所有操作的进度条通知。

还包括允许根据执行操作时发生的情况进行交互的按钮，例如关闭按钮。

只要没有正在进行的操作，就可以使用 Esc、Alt+F4 或通过切换到关闭按钮来关闭插件。

## 插件包生成

选择这个分类后按 Tab 键，焦点会停留在一个列表，里面有安装的所有插件，不管是启用的、禁用的还是不兼容的。

也可以使用 Alt+L 快速跳转到此列表，使用空格键选中所有想要选择的插件，以便在选择的文件夹中制作备份副本。

每个插件都将以其名称和版本以及识别标签“_gen”生成，这些生成的插件可以毫无问题地与 NVDA 一起安装。

继续按 Tab 键，将切换到一个名为选择的按钮，或者可以使用 Alt+S 快速访问该按钮，按下该按钮，将显示一个菜单，可以快速选择或取消选择所有插件。

再次按 Tab 键，将切换到生成按钮或按 Alt+G 快速访问，至少选中一个插件后按下该按钮，将打开一个窗口以选择要保存所选插件的文件夹。

选择文件夹后，将开始生成插件。焦点将停留在一个只读框中，其中将显示正在操作的信息以及一个进度条。在生成插件的操作完成之前，关闭按钮以及界面的其余部分将被禁用。

操作完成后，会通知是否成功或出现问题，按 Tab 键可选择确定 (Alt+O)、取消 (Alt+C) 或根据需要关闭界面。

确定和取消按钮将根据操作完成的方式出现。

要生成插件，必须至少选中一个插件，否则将收到一条错误消息。

## 批量安装

这个类别将允许选择一个存放多个插件的文件夹，可一次性安装。

当进入这个类别时，将切换到一个名为“选择插件所在文件夹...”的按钮，按下该按钮，将打开一个窗口用以选择包含插件的文件夹。

在选择文件夹之前，此类别中的其余界面将被禁用。

选择文件夹后，焦点将留在只读框中，用以在搜索插件时提示当前操作，还将从进度条中收到信息。

搜索完成后，将被告知是否存在问题以及如何采取行动。只接受符合当前 NVDA API 的插件，丢弃任何不兼容或损坏的插件。

搜索完成后，如果找到插件，按“确定”后，列表将被激活，其中包含在所述文件夹中找到插件的名称。

可以使用 Alt+L 快速转到该列表，在这个列表中可用空格键选中任意数量的插件。

按 Tab 键，将切换到与插件包生成页面相同的选择按钮，继续按 Tab 键，将切换到安装按钮，可按 Alt+I 快速访问该按钮。

选择至少一个插件后按下该按钮，将执行一个或多个插件安装，而不会显示经典的 NVDA 安装窗口，这样可以加快插件的安装速度。

当按下安装按钮后，焦点将停留在一个提示当前操作的只读框中

同样，当完成时，将会告知您是否成功，或者是否有无法安装的插件或错误。

根据发生的情况，将启用关闭按钮旁边的确定或取消按钮。

如果启用了确定按钮，则 NVDA 已经安装插件，并且要应用这些插件，需要重启 NVDA。如果按下该按钮，NVDA 将重新启动并且加载已经安装的插件。

如果取消并关闭，在 NVDA重启前，将无法再次使用该插件，。这是避免重复操作的保护措施。

如发生故障，则只出现取消按钮，可以按下该按钮，会返回到之前的界面。

### 警告

实现该类别是为了加快插件的安装速度，但是错误的安装插件会导致 NVDA 出现故障。用户应正确使用该功能。

## 卸载插件

此类别将可快速卸载插件。

可以从列表中按空格键选中已安装的任何插件。

还有一个选择按钮，其实现的功能与前面的类别完全相同。

继续按 Tab 键，会切换到卸载按钮，如果选择了一个或多个插件后按下该按钮，焦点将停留在一个提示当前操作的只读框中。

同时也会通过进度条得到通知。

完成后，插件会通知结果，就像在批量安装类别中一样，会有确定按钮，通知需要重新启动 NVDA 或取消按钮，通知出现错误，或关闭按钮，用以关闭插件窗口。

请注意，如果关闭此类别并且没有注意重新启动插件的提示，那么在 NVDA 重新启动之前此插件将无法再次使用。

### 警告

一旦按下了卸载按钮，插件的卸载将不可逆，所以应确保知道从哪里获得已经删除的插件，以防想要重新安装它们，以及包含插件目录本身中的信息，此类信息将被删除。

这通常不是好的做法，NVDA 不建议插件将信息保存在与插件相同的目录中，但这是插件开发者的决定。

因此，使用此类别需要您自担风险。

## 启用/禁用插件

这个类别将允许批量启用或禁用插件。

进入该类别，焦点将停留在已启用的插件列表中，可以使用 Alt+L 快速访问该列表，使用空格键选中想要禁用的插件。

如有禁用的插件，那么还会有一个包含这些插件的列表，可以使用空格键选中想要启用的插件。

可以在两个列表中分别选中插件，这些操作将反向执行，禁用那些在已启用的插件列表中选中的插件，并启用那些在已禁用的插件列表中选中的插件。

这个类别也有一个选择按钮，但有一些不同，当按下该按钮时，将包含每个列表的子菜单，能够为选择的列表选择或取消选择所有内容。

按 Tab 键，会找到应用按钮或按 Alt+P 快速访问，如果按下该按钮，它将把焦点留在提示当前操作的只读框中。

操作完成后，就会像之前的类别一样通知并激活相应的按钮。

## 清单修改

在此类别中，可以更改清单，从而使插件与 NVDA 所需的 API 兼容。可以更改已安装的插件或 NVDA 插件包文件的清单。

根据最新的 NVDA 政策，每年在第一个 NVDA 版本发布后，插件开发者都必须更改插件版本以使其清单与 NVDA 版本相匹配。

会有开发者立即更改，其他人需要一段时间，还有部分开发者由于放弃插件或其他原因根本不会做。

在最后一种情况下，将不得不手动更改 lastTestedNVDAVersion 属性，如果有大量插件需要更改，将浪费许多时间。

此外，如果想要测试 Beta 版和 RC 版，将必须在清单中更改此参数，否则将无法安装插件。

这意味着更改清单中的日期可以暂时解决一些问题，以便能够继续使用那些未更新的插件。但是会有插件不仅需要更改清单，还需要内部更改以适应新版本，在这种情况下，插件将崩溃，此时就需联系所述插件的作者了。

强烈建议更新更改清单后出现的插件，因为这些插件可能会带来除了更改清单之外开发者所做的其他修改。

访问此类别后，焦点将停留在列表，该列表将包含已安装的所有插件及其 API 版本。可以按空格键选中想要更改清单的插件。

继续按 Tab 键，将分别切换到三个组合框：

* 选择主要版本：此组合框必须与 NVDA 将要更新的版本日期相匹配。

* 选择次要版本：这里通常选择1即可，但 NVDA 每年发布四个版本，故亦可选择其他值，以防有其他变化。

* 选择修订版本：这里选择 0 即可，但为了以防万一，其值最高可选择为 9。

继续按 Tab 键，将切换到选择按钮，允许选择或取消选择列表中的所有插件。

再次按 Tab 键，将切换到应用按钮，或使用 Alt+P 快速访问该按钮。

，如果按下这个按钮，将显示一个菜单，其中包含以下选项：

* 处理并安装，如果选择此选项，会将已安装的插件列表中选中的插件清单更改为主要版本、次要版本和修订版本组合框中选择的值。

* 处理插件文件，如果选择此选项，将打开一个打开文件对话框，必须在其中选择要更改清单的插件包。之后会将该插件清单更改为主要版本、次要版本和修订版本组合框中选择的值。

如果选择处理插件文件并且操作成功，那么在插件包的所在文件夹中将生成一个具有相同名称并且带有“_gen_modify_manifest”标签的插件，这即是修改清单后的插件。

这两个选项中的任意一个被激活，焦点都将停留在操作提示的只读框中。

请注意，必须在选中插件文件之前，更改主要版本、次要版本和修订版本的组合框，以便将所述配置应用于选择插件的清单文件。

### 警告

使用该类别的一切结果完全由用户负责。

## 备份恢复

该类别将在列表中显示可以制作备份副本的选项。

此版本中可以保存在备份副本中的选项包括：

* 字典文件夹 \speechDicts
* 配置文件夹 \profiles
* 便签文件夹 \scratchpad
* 配置触发文件 profileTriggers.ini
* 按键与手势配置 gestures.ini
* NVDA 设置 nvda.ini

该列表将仅显示在 NVDA 副本中存在的选项以及具有内容的文件夹。

例如，如果配置文件夹为空，则不允许备份。

至少从列表中选择一项才能制作备份副本。

继续按 Tab 键，会切换到两个按钮：

* 创建备份

如果按下该按钮，一个经典的 Windows 保存对话框将打开，输入备份的名称以及想要保存它的位置。

当按下保存时，备份将开始，并且在只读框中提示操作是否成功。

* 恢复备份

按下该按钮，将打开一个经典的 Windows 对话框以浏览备份文件。

文件打开后，将显示一个包含已备份内容的窗口，在该窗口中将出现一个列表以选择希望恢复的选项。

当需要时，按下恢复按钮，会在只读框中提示是否恢复成功。

### 警告

当恢复 NVDA 配置后，需要重启 NVDA，因此无论按下确定、取消还是关闭按钮，都将重启 NVDA。

如果在恢复多个配置时发生错误而只恢复了部分配置，NVDA 也将重启。

## 插件文档

可以通过此类别查阅插件作者编写的文档，以了解如何使用插件。

在此类别中，将有一个列表，其中将显示所有具有文档的插件，不包括出于任何原因没有文档的插件。

继续按 Tab 键，会切换到打开插件文档按钮，按下该按钮，将用默认浏览器打开列表中所选的插件文档

## NVDA 未响应时关闭

这个新选项没有分配界面和快捷键。

为此，必须转到 NVDA 的按键与手势对话框 ➡ NVDA 插件实用程序 ➡ NVDA 未响应时关闭，并为其分配一个快捷键。

按下该快捷键将关闭 NVDA。

# 译者和合作者：

如果有人想翻译或合作，他们可以通过插件的 Github 存储库或发送电子邮件至 xebolax@gmail.com 来实现

* 英语：Dragan Ratkovich（文档机器翻译）
* 土耳其语：umut korkmaz
* 法语：Rémy Ruiz
* 阿拉伯语：Wafiq Taher
* 德语：Moritz Wolfart
* 俄语：Valentin Kupriyanov（NVDA.RU 俄语社区）
*意大利语： Leonardo Marenda
* 乌克兰语：Vova Mobile

# 更新日志。
## 有关更新的信息：

该插件将遵循以下更新路径：

此历史记录中仅列出 major.minor 版本（例如 v3.1）。

major.minor.x 类型的版本（例如 v3.1.2）是翻译更新。

对插件的更改将反映在解释新增功能的部分中。

主文档不会被修改，因为它是用户的方向。

用户有责任查看此部分以了解更改。

## 版本 1.5。

* NVDA 未响应时关闭

这在 NVDA 崩溃时很有用。

有一个名为 Kill NVDA 的插件也可关闭 NVDA。Kill NVDA插件和此插件中的这个内置函数的区别在于，前者使用系统工具，而后者直接调用 Windows 内核，因此更强大，更可靠。

## 版本 1.4。

兼容 NVDA 2023.1。

## 版本 1.3。

* 修复了生成插件时的错误。

新版本的 NVDA 会在插件目录中生成 __pycache__ 文件夹。在这个版本的插件中，生成的插件将与开发者分发的插件相同，不包括该文件夹。

## 版本 1.2。

* 修复了备份中的严重错误。

## 版本 1.1。

* 修正错误。

* 添加了备份和恢复功能。

## 版本 1.0。

* 初始版本。

随着新功能的添加，旧的插件已从头开始重写。

该插件已重命名为 NVDA 插件实用程序，但仍保留由 NVDA 处理的内部名称 addonPackager。

启动此版本时，cricricri 插件将不再维护，因为此插件已包含清单更改。