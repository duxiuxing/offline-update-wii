# Step 3: 安装 cIOS236  {#step3}


本文重在阐述安装步骤，相关知识点请参考[《IOS36 和 cIOS236》](../cios236/README.md)。

## 一、相关文件

| 文件 | 出处 |
| --- | --- |
| Multi-Mod Manager（以下简称 MMM） | <https://gbatemp.net/download/multi-mod-manager.13015> |
| IOS15-64-v257.wad | 通过 NUS Downloader 下载 |
| IOS15-64-v1032.wad | 通过 NUS Downloader 下载 |
| IOS36-64-v3608.wad | 通过 NUS Downloader 下载 |
| cIOS236[36-v3351]-v65535.wad | <https://modmii.github.io> <br/>cIOS236 的安装文件，基于 IOS36-64-v3351 制作 |


## 二、注意事项

- 如下图所示，如果 -> Load another IOS 后面的文字带有 IOS236 的字样，说明你的 Wii 已经安装过 cIOS236，可以直接略过本文余下的内容，直接跳转到[《Step 4: 安装 IOS58》](@ref step4)，继续后面的操作：<br/>
  ![](./mmm-cios236-loaded.png)

- IOS36-64-v3608.wad 是最新的 IOS36 安装文件，MMM 将基于它制作出 cIOS236；

- 如果你在 MMM 中无法使用遥控器手柄，在 `apps/MMM` 文件夹里有一个 cIOS236 的安装文件（.wad 格式），请参照[《Step 2: 安装 USB Loader 使用的 cIOS》](@ref step2)一文中的做法完成安装：<br/>
  ![](./yawmME-select-cios236.png)


## 三、安装步骤

1. 在 HBC 运行 MMM ：<br/>
  ![](./multi-mod-manager.png)

2. 先按遥控器手柄的方向键，使 -> 指向 Load another IOS，然后按 [A] 键：<br/>
  ![](./mmm-load-another-ios.png)

3. 先选中 249，然后按 [A] 键：<br/>
  ![](./mmm-select-cios249.png)

4. 先按方向键，使 -> 指向 Install & Patch IOS36，然后按 [A] 键：<br/>
  ![](./mmm-cios249-loaded.png)

5. 先确认 --> 指向 Express mode，然后按 [A] 键：<br/>
  ![](./mmm-express-mode.png)

6. 耐心等待安装结束：<br/>
  ![](./mmm-install-cios236.png)

7. 按任意键回到 MMM 的主界面，可以看到当前使用的 IOS 为 IOS236:<br/>
  ![](./mmm-cios236-loaded.png)


有了 cIOS236 的加持，我们可以使用 MMM 的 WAD Manager 来安装任何 .wad 文件，正如上文第 6 步最后的提示信息所言：

> You can use it to install anything now.
