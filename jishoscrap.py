from bs4 import BeautifulSoup
import requests

kanjilist = requests.get('http://nihongo.monash.edu/jouyoukanji.html', auth=('user', 'pass'))
print(kanjilist.status_code)
soup = BeautifulSoup(kanjilist.text)
#print(r.text)
print(soup.title)

kanji = soup.title
print(type(kanji))
kanji = str(kanji)
print(type(kanji))

print(kanji)

grade1 =  "一 九 七 二 人 入 八 力 十 下 三 千 上 口 土 夕 大 女 子 小 山 川 五 天 中 六 円 手 文 日 月 木 水 火 犬 王 正 出 本 右 四 左 玉 生 田 白 目 石 立 百 年 休 先 名 字 早 気 竹 糸 耳 虫 村 男 町 花 見 貝 赤 足 車 学 林 空 金 雨 青 草 音 校 森"
print(grade1)
grade2 = "刀 万 丸 才 工 弓 内 午 少 元 今 公 分 切 友 太 引 心 戸 方 止 毛 父 牛 半 市 北 古 台 兄 冬 外 広 母 用 矢 交 会 合 同 回 寺 地 多 光 当 毎 池 米羽 考 肉 自 色 行 西 来 何 作 体 弟 図 声 売 形 汽 社 角 言 谷 走 近 里 麦 画 東 京 夜 直 国 姉 妹 岩 店 明 歩 知 長 門 昼 前 南 点 室 後 春 星 海 活 思 科 秋 茶 計 風 食 首 夏 弱 原 家 帰 時 紙 書 記 通 馬 高 強 教 理 細 組 船 週 野 雪 魚 鳥 黄 黒 場 晴 答 絵 買 朝 道 番 間 雲 園 数 新 楽 話 遠 電 鳴 歌 算 語 読 聞 線 親 頭 曜 顔"
print(grade2)
grade3 = "丁 予 化 区 反 央 平 申 世 由 氷 主 仕 他 代 写 号 去 打 皮 皿 礼 両 曲 向 州 全 次 安 守 式 死 列 羊 有 血 住 助 医 君 坂 局 役 投 対 決 究 豆 身 返 表 事 育 使 命 味 幸 始 実 定 岸 所 放 昔 板 泳 注 波 油 受 物 具 委 和 者 取 服 苦 重 乗 係 品 客 県 屋 炭 度 待 急 指 持 拾 昭 相 柱 洋 畑 界 発 研 神 秒 級 美 負 送 追 面 島 勉 倍 真 員 宮 庫 庭 旅 根 酒 消 流 病 息 荷 起 速 配 院 悪 商 動 宿 帳 族 深 球 祭 第 笛 終 習 転 進 都 部 問 章 寒 暑 植 温 湖 港 湯 登 短 童 等 筆 着 期 勝 葉 落 軽 運 遊 開 階 陽 集 悲 飲 歯 業 感 想 暗 漢 福 詩 路 農 鉄 意 様 緑 練 銀 駅 鼻 横 箱 談 調 橋 整 薬 館 題"
print(grade3)
i = 0
for item in grade1:
    i+=1
for item in grade2:
    i+=1
for item in grade3:
    i+=1
print(i)
#print(tag)