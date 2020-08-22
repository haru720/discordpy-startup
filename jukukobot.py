import discord
import os

# 接続に必要なオブジェクトを生成
client = discord.Client()

async def greet():
    channel = client.get_channel(743788202543808583)
    await channel.send('起動')
    
@client.event
async def on_ready():
    await greet()



@client.event
async def on_message(message):
    if message.content == 'ポア':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('ポアします')
        else:
            await message.channel.send('修行しなさい')


    elif message.content == "十月祭":

        await message.channel.send("女子高の文化祭。名前通り、神無月に行われる。その実態は猛烈な勧誘の嵐。さながら、新宿歌舞伎ｔ（ｒｙ......。")

    elif message.content == "塾高":

        await message.channel.send("天下")

    elif message.content == "日吉烏":

        await message.channel.send("キャンパス内に巣の存在が複数確認されており、時折（特に夕方）けたたましい鳴き声を上げながら大群が上空を旋回する。塾高生がポテトを落としてから、くちばしに咥えて持ち去るまでのスピードには目を見張るものがある。")

    elif message.content == "まむし谷階段":

        await message.channel.send("校舎から直接まむし谷に行く唯一の道。かなり急である。部活後の人々にとってあれほど面倒なものはない。まさに「行きはよいよい・帰りはつらい」である。")

    elif message.content == "医学部":

        await message.channel.send("塾高では超エリートのみが進学を許される最強学部。外部入学は基本浪人です。")

    elif message.content == "オワTA":

        await message.channel.send("「終わった」の派生語である「オワタ」がさらに派生した語。")

    elif message.content == "意見箱":

        await message.channel.send("生徒会室前につるしてある木の箱。紙に書いた意見を入れると生徒会に届き、場合によっては先生にも届く…らしい。監査局付近にも似た箱があるので注意。なお塾高生からその存在は忘れ去られている。2018年から担当の部署もでき期待できる…かも？")

    elif message.content == "漢":

        await message.channel.send("生き様が立派な、「こいつこそ男の中の男だ！」を定義とした代名詞。")

    elif message.content == "エグい":

        await message.channel.send("つらい、きつい、の塾語表現。代表的な塾語であり、毎年無理して使いたがる新入生のさまは見ていてエグい。広義では「グロテスク」の意味で用いられたりする。動：「エグる」")

    elif message.content == "シコい":

        await message.channel.send("勤勉なさまをちゃかした非道徳的形容詞かつ代表的な塾高用語。テニス用語の「シコラー」からの派生語と言われる。公共の場で用いると妙な誤解を招きかねないので気をつけよう。てか外では決して使うべからず。関連語: シコ勉、シコる、用例: シコってんじゃねーよ")

    elif message.content == "disる":

        await message.channel.send("disrespectの略。軽蔑すること、相手を貶める発言をすること。耳にする機会も多いはず。")

    elif message.content == "愛":

        await message.channel.send("ってなんだ？知ってる人は知っているらしい。適度の補給は必要でしょう。でもここは男子校、がんばろう...な？")

    elif message.content == "オープンリーチ":

        await message.channel.send("中間試験でいきなり悪い成績をたたき出し、留年勧告されること。これを受けたものはクラスの英雄になれる。")

    elif message.content == "ダダ":

        await message.channel.send("ひようら・普通部通りにある古本・貸本屋ダダ書房。店先には怪しげな本が並んでいるが、文庫本や古書が充実している。店番のおばあさんからも、ただものではない雰囲気が感じられる。")

    elif message.content == "志木高":

        await message.channel.send("姉妹校ならぬ兄弟校・慶應義塾志木高等学校の略称。埼玉県志木市に位置する。全校生徒数は750名。塾高生からはなぜか田舎扱いされている。実際志木はいなk(ry")

    elif message.content == "北側":

        await message.channel.send("北側の玄関ホール。アイスホッケー部の物置になっており、無数のバッグが散乱している。南側はサイクリング部で、同じ状況にある。")

    elif message.content == "ガチ勢":

        await message.channel.send("期末テストや運動会などに真剣に取り組む人々の総称。ほかにも厄介勢や、ネタ勢等〇〇勢とつく塾語は多い")

    elif message.content == "避難訓練":

        await message.channel.send("年に一回開催される防災訓練。消防法で実施が義務付けられているらしいが、雨だと延期になることもある。南側グラウンドに全校生徒が集合した後は、校長先生の素晴らしい話が聞ける。生徒数の都合上、避難完了に30分かかっても非常に迅速という評価である。")

    elif message.content == "日吉祭":

        await message.channel.send("塾高における文化祭。ナンｐ…文化祭としては、日本トップクラスの規模と予算と入場者数と迫力とクオリティとチャラさを誇る。")

    elif message.content == "急降下":

        await message.channel.send("授業開始から5分以上教員がこないときに用いる。語源は「休講か？」から。")

    elif message.content == "生徒会":

        await message.channel.send("塾高では影の薄い存在ではあるが、実は生徒全員が会員である大きな組織。役員の仕事内容は新世紀該当ページを参照。将来に向けて社会勉強したい方、自制心を養いたい方、とりあえず何かしらの肩書が欲しい方は、生徒会室の扉を叩こう。")

    elif message.content == "昨日テスト勉強してねー":

        await message.channel.send("実は徹夜でテスト勉強に勤しんでいた者の常套句。時代の波に左右されない。学生間の永久流行語であり、塾講もその例に漏れない。主にテストの結果が芳しくなかった場合の保険として用いられる。")

    elif message.content == "名門":

        await message.channel.send("援部（含吹奏楽等）の人物紹介の際、出身校コールに対する観客のレスポンス。普通部中等部に限らず、地元の公立高校も、どんな荒れた中学校であっても名門であることに疑いの余地はない。")

    elif message.content == "印刷室":

        await message.channel.send("生徒会の究極兵器（アルテマウェポン）・・・だったものの、いつからかなくなり倉庫に。かなり汚かったらしい・・・窓もないしね。")

    elif message.content == "通勤特急":

        await message.channel.send("東横線の列車種別の一つ。特急と言いながら日吉にも停まってくれる。平日の朝夕のみ運転される。朝の下りで寝過ごすと遅刻不可避なので気をつけましょう。")

    elif message.content == "厄介":

        await message.channel.send("「面倒」をはるかに超越した事態・人物の総称。とてつもない量の宿題が出た場合や、他人との絡みがあまりに執拗な場合にこう呼ばれる傾向にある。")

    elif message.content == "除籍":

        await message.channel.send("約20年前までは存在していた処罰。退学をも凌駕するその驚異の内容は、塾高に在籍していた証拠ごと抹消されるというものである。つまり、除籍処分を受けると中卒扱いとなってしまう。高3でこれを食らったら痛いのなんの…")

    elif message.content == "SFC":

        await message.channel.send("慶應義塾湘南藤沢キャンパスの略。施設はかなり充実しているが、塾内での学費の大半を開発費と医学部に当てているという噂は聞き逃せない。")

    elif message.content == "OpenChat":

        await message.channel.send("LINEのOpenChatです。参加はこちらのURLからどうぞ!/https://t.co/1EjHGekbnO?amp=1")

    elif message.content == "ガン萎え":

        await message.channel.send("天下")

    elif message.content == "チャイ語":

        await message.channel.send("天下")

    elif message.content == "独語":

        await message.channel.send("ひとりごとではない。2,3年次のドイツ語選択のこと。第二外国語で一番人口が少なく、またテストの平均が一番高い。音楽選択―ドイツ語選択は治安最高峰。ちなみに担当教員は責任時間が足りないようで、英語も掛け持ちしている。お疲れ様です。")

    elif message.content == "アツい":

        await message.channel.send("モチベーションの急上昇を煽るエキサイティングな事象に直面した際に用いる。")

    elif message.content == "GHQ":

        await message.channel.send("「Go Home Quickly」の略。コードネーム: KITAKUBU")

    elif message.content == "性教育":

        await message.channel.send("生協に行くこと。ちなみに、走っていく場合は「Dash 生協」（元ネタはかの有名な「應」援歌）。")

    elif message.content == "GTEC":

        await message.channel.send("毎年夏休み前後に行われるベ〇ッセ主催の(笑)なテスト。それはわざわざ「真剣に受験してください」のアナウンスが流れるほどである。")

    elif message.content == "キャリーオーバー":

        await message.channel.send("数学科H先生が用いる評点の付け方。前期に20A以上の成績が付いた場合、その余り分を後期の成績に付け加えるというもの。ただ、高確率で後期も20Aをとるので、あまり意味が無かったりする。")

    elif message.content == "並木ダッシュ":

        await message.channel.send("8:18-8:22にかけて銀杏並木で繰り広げられる、遅刻回避をかけた汗と涙の感動のドラマ。晩秋の銀杏並木にて行われる様子は、非常に幻想的である。/ちなみにタイムリミットは/下り8:16 各停（大概遅れる）/上り8:18 通特（大概遅れる）")

    elif message.content == "4649":

        await message.channel.send("化学科K本先生の決め台詞。ここは覚えてね、という意味でよくつかわれる。生徒から「着ボイスにしたい」と非常に好評である。")

    elif message.content == "ウツシスト":

        await message.channel.send("数学科O山先生による業界用語で、他人のプリントを写す人を意味する。ただし考えずに写している人がほとんどであるため、学習効果は不明である。")

    elif message.content == "チキる":

        await message.channel.send("恐れをなして行動を起こすのを躊躇すること。英語のChickenに由来する。これも代表的な塾語のひとつである。")

    elif message.content == "ラスTO":

        await message.channel.send("体連などで使われる「ラスト一本!!」の「ラスト」が派生した語。")

    elif message.content == "カーディガン":

        await message.channel.send("なぜか校則によって着用が禁止されている。教員に理由を尋ねても「よくわからないけどダメなものはダメ」の一点張り。イギリスでは昔、正式な場でのカーディガンは認められていなかったからという説も...。塾高の七不思議のひとつ。ほかの七不思議は知りません。")

    elif message.content == "球技大会":

        await message.channel.send("毎年6月ごろ、学年別クラス対抗でスポーツの覇を競う行事。バスケ・バレー・ソフトボール・サッカー・卓球から1種目選び参加することを義務付けられている。体育科の教員が当たった場合、勝敗が成績に関与する可能性もある。")

    elif message.content == "ソロ":

        await message.channel.send("一人で何かの行動をすること。ぼっちとはちがいます。いいですか、ぼっちとは違います。（大事なことなので2回言いました）")

    elif message.content == "ローソン":

        await message.channel.send("協生館のコンビニ。毎日夕方や夜にかけ、体連をはじめとした生徒たちが、樹液を求める昆虫のごとく集まる。昼休みに強襲する猛者もいるが、本来は許可願が必要である。")

    elif message.content == "キレそう":

        await message.channel.send("うまくいかずにストレスが溜まっている状態。これを言葉に出すことによってイライラを解消している。")

    elif message.content == "目黒線":

        await message.channel.send("2008年、日吉まで延伸してきた路線。日吉が起点・終点であるため、寝過ごして大丈夫＆乗るときは座れる。なお2022年度末にS鉄と繋がる予定。急行も走っているが、日吉から目黒13駅中8駅も停車する。また、登校時武蔵小杉行きに総合するとガン萎えする。")

    elif message.content == "ビデオ収納庫":

        await message.channel.send("各階に存在する、ビデオ機材を収納する倉庫。しかし「ヒデオ収納庫」「ヒテオ収納庫」などと改造されまくってる現在、初期状態で残っているものは極めてレアである。南京錠によってロックされているものの、それはカモフラージュ、実際は容易に開くとか…?")

    elif message.content == "A.J.Y":

        await message.channel.send("「A：あとはJ：じぶんでY：やっといて」の略。数学科I塚先が板書で多用する。定義せず黒板に突然現れたら、本botで得た知識を存分にひけらかしてほしい。")

    elif message.content == "落生":

        await message.channel.send("留年生のこと。2周目にして成績が振るわないのが定例であるクラス内では一応先輩扱いとなる場合もあるが、ごくまれに後輩未満の不当な扱いを受けることも。留学からの帰国生も扱われることもある。")

    elif message.content == "大宮":

        await message.channel.send("埼玉県の主要都市（現在は区に降格）でありながら、塾高生からはなぜか田舎呼ばわりされている聖域。実際日吉の方がいな(ry")

    elif message.content == "シモダッシュ":

        await message.channel.send("下田に活動拠点のある体連の人々が練習に遅れないように頑張ってダッシュすること。")

    elif message.content == "レべチ":

        await message.channel.send("「レベルが違う」の略。")

    elif message.content == "LUCKY BOX":

        await message.channel.send("数学O山先生の授業などで用いられる業界用語であり、O山先生の教卓に置かれている箱を指す。プリント提出のために用いられ、試験前には入りきらなくなるほどプリントがたまることもしばしば。")

    elif message.content == "それな":

        await message.channel.send("相手の発言に同意する場合に使う。ただし多用すると会話が続かなくなるため、用法容量正しく守って使いましょう（逆に会話を切りたいときに使うと効果的）。")

    elif message.content == "入試バイト":

        await message.channel.send("例年志願者が殺到する、2月に行われる塾高の入学試験の手伝いをするバイト。/対象は3年生のみ。報酬は4日間約25時間労働約20,000円。毎年70名が採用され、無遅欠、近所（30分以内と噂される）じゃないと採用は厳しいらしい。/なお最低賃金。")

    elif message.content == "バリューセット":

        await message.channel.send("地下食堂の人気メニュー。ドリンクとポテトにナゲットが付くAセットと、コロッケがつくBセットがある。ナゲットの品薄のため、しばしば唐揚げが混ざる。とあるクラスでは購入した者を待ち伏せして強奪するものまでいる。ちなみにおすすめはAセット。")

    elif message.content == "クロカン":

        await message.channel.send("体連の部活がランニングコースとして塾高の周囲や、下った先の蝮谷を走るメニューのこと。部活によってルートが少し違う。")

    elif message.content == "裏":

        await message.channel.send("留年した後。学年2周目。各学年一回ずつ裏を回ることができる。")

    elif message.content == "車部":

        await message.channel.send("40年の歴史を誇る、日本で唯一の部活。普通乗用車を用いて、日々ドライブテクニックを磨いているらしい団体。ある種の薬物の名と混同しやすいので注意。")

    elif message.content == "チャキる":

        await message.channel.send("親からもらった昼食代を、一食抜かすなどして着服すること。一か月ぐらい皮算用しているひとをよく見かけるが、達成した漢は見たことがない。")

    elif message.content == "卒研":

        await message.channel.send("3年次に行う卒業研究のこと。興味のあるテーマを自分で決め、1年を通して研究する。これに合格しなければ、成績の如何を問わず卒業ができない。なお2016年度よりテーマ設定の自由度が高くあった。適当に選ぶと痛い目に遭うのは言うまでもない。")

    elif message.content == "ピーナッツ":

        await message.channel.send("落生の隠語。（落生⇒落下生⇒落花生）")

    elif message.content == "日吉蚊":

        await message.channel.send("日吉に生息する蚊。幸か不幸か塾高生の血を主食としている。")

    elif message.content == "SSH":

        await message.channel.send("文科省によって認定されており、理系科目において国からの援助を受けている学校。塾高も認定されて「いた」。")

    elif message.content == "授業日数":

        await message.channel.send("本校はヤスミが多く、高等学校としては法的にぎりぎりの日数しか授業がない、つまりあと数日でも授業日数が少ないと専門学校扱いになる…という都市伝説がある。選択旅行も授業日数に含まれるためらしい。ちなみに出席日数の如何によっては留年もありうる")
  
client.run(os.environ.get('ENV_VAR_DISCORD_ID'))
