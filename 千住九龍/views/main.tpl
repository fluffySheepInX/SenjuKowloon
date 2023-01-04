
% rebase('layout2.tpl', title='千手九龍', year=year, divBaseColor=divBaseColor)

<div class="normalBlock ">
	【千手九龍】
	>
	<button type=“button” onclick="location.href='./top'">
	Topへ戻る
	</button>
	>
	<button type=“button” onclick="location.href='./main'">
	更新
	</button>
	>>>襲撃解除月は「2019/10/26」です　※コマンド「襲撃」が実際に可能になるゲーム内年月です。
</div>
<br />
<div class="flexcontainer">
		<div class="flexitem item1">
			<div class="tabs">
				<input id="map" type="radio" name="tab_item" onclick="sendByAjaxLeft(1)" {{!checkedLeft1}}>
				<label class="tab_item" for="map">マップ・情勢</label>
				<input id="command" type="radio" name="tab_item" onclick="sendByAjaxLeft(2)" {{!checkedLeft2}}>
				<label id="commandLabel" class="tab_item" for="command">コマンド</label>
				<input id="quest" type="radio" name="tab_item" onclick="sendByAjaxLeft(3)" {{!checkedLeft3}}>
				<label class="tab_item" for="quest">その他</label>
				<div class="tab_content" id="map_content">
					<div class="tab_content_description">
						<section>
							<div>
								<br />
								<form action="./meetingRoom">
									<button type="submit">会議室</button>
								</form>
								<br />
								<details>
									<summary>
										マップ
									</summary>
									<br />
									{{ !currentLocation }}
									<br />
									<details>
										<summary>
											防衛
										</summary>
										<br />
										{{ !guard }}
										<br />
									</details>
									<br />
									{{ !map }}
								</details>
								<details>
									<summary>
										情勢
									</summary>
									<br />
									{{ !news }}
									<br />
								</details>
								<details>
									<summary>
										ステータス
									</summary>
									<br />
									{{ !status }}
									<br />
								</details>
								<details>
									<summary>
										特殊
									</summary>
									<br />
									<form action="./listSoldier" method="post">
										<button type="submit">兵一覧</button>
									</form>
									<br />
									<!--
									<form action="./weapon" method="post">
										<button type="submit">武器更新</button>
									</form>
									-->
									<br />
									<form action="./historyAction" method="post">
										<button type="submit">行動履歴</button>
									</form>
									<br />
									<form action="./questCommon" method="post">
										<button type="submit">クエスト【共通】</button>
									</form>
									<br />
									<!--
									<button type=“button” onclick="location.href='./main'">クエスト【陣営】</button>
									-->
								</details>
								<br />
								<form action="./config" method="post">
									<button type="submit">設定画面</button>
								</form>
								<br />
								<br />
								{{ !appointment }}
							</div>
						</section>
						<br />
					</div>
				</div>
				<div class="tab_content" id="command_content">
					<div class="tab_content_description">
						<form name="actionCommand" action="./inputAction" method="post">
							{{ !action }}
							{{ !command }}
							<br />
							<input type="button" value="All Command" onclick="clickBtnAll()"/>
							<input type="button" value="Even Command" onclick="clickBtnEven()"/>
							<input type="button" value="Odd Command" onclick="clickBtnOdd()"/>
							<br />
							<button type="submit">入力</button>
						</form>
					</div>
				</div>
				<div class="tab_content" id="quest_content">
					<div class="tab_content_description">
						<details>
							<summary>
								管理へのお便り
							</summary>
							<br />
							<button type=“button” onclick="location.href='./main'">工事中</button>
							<br />
							<br />****
							<br />大変なことになりましたら、
							<br />ツイッターにて一報下さると幸いです。
							<br />※アカウントへのリンクはログイン画面の「ドキュメント」の一番下にあります。
							<br />****
						</details>
					</div>
				</div>
			</div>	
		</div>
		<div class="flexitem item1">
			<div class="tabs">
				<input id="chatAll" type="radio" name="tab_item2" onclick="sendByAjaxRight(1)" {{!checkedRight1}}>
				<label class="tab_item" id="tab_item_chat_all" for="chatAll">全体へ{{!countAll}}</label>
				<input id="chatGroup" type="radio" name="tab_item2" onclick="sendByAjaxRight(2)" {{!checkedRight2}}>
				<label class="tab_item" id="tab_item_chat_group" for="chatGroup">所属へ{{!countGroup}}</label>
				<input id="chatPrivate" type="radio" name="tab_item2" onclick="sendByAjaxRight(3)" {{!checkedRight3}}>
				<label class="tab_item" id="tab_item_chat_private" for="chatPrivate">個人へ{{!countPersonal}}</label>
				<div class="tab_content" id="chatAll_content">
					<div class="tab_content_description">
						<form action="./chatAll" method="post">
							<textarea cols="30" rows="10" name="remark"></textarea>
							<br />
							<button type="submit">送信</button>
						</form>
						{{ !chatAll }}
					</div>
				</div>
				<div class="tab_content" id="chatGroup_content">
					<div class="tab_content_description">
						<form action="./chatGroup" method="post">
							<textarea cols="30" rows="10" name="remark"></textarea>
							<br />
							<button type="submit">送信</button>
						</form>
						{{ !chatGroup }}
					</div>
				</div>
				<div class="tab_content" id="chatPrivate_content">
					<div class="tab_content_description">
					<form action="./chatPrivate" method="post">
						<textarea cols="30" rows="10" name="remark"></textarea>
						<br />
						未実装ご容赦
						<br />
						<!--<button type="submit">送信</button>-->
					</form>
					{{ !chatPrivate }}
					</div>
				</div>
			</div>
		</div>
</div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
function sendByAjaxLeft(args) {
	$.ajax({
	    type: "POST",
	    url: "{{!ajaxUrlLeft}}",
	    data: {"target":args,"id":"{{ !id }}","password":"{{ !password }}"},
	})
	.done(function (response, textStatus, jqXHR) {
		console.log(response);
		if (response.status === "err") {
		    //alert("err: " + response.msg);
		} else {
		    //alert("OK");
		}
	    })
}
function sendByAjaxRight(args) {
	$.ajax({
	    type: "POST",
	    url: "{{!ajaxUrlRight}}",
	    data: {"target":args,"id":"{{ !id }}","password":"{{ !password }}"},
	})
	.done(function (response, textStatus, jqXHR) {
		console.log(response);
		if (response.status === "err") {
		    //alert("err: " + response.msg);
		} else {
		    //alert("OK");
			if(args==1){
				document.getElementById("tab_item_chat_all").innerText = "全体へ"
			}
			if(args==2){
				document.getElementById("tab_item_chat_group").innerText = "所属へ"
			}
			if(args==3){
				document.getElementById("tab_item_chat_private").innerText = "個人へ"
			}
		}
	    })
}


function clickBtnAll(){
	const target = document.actionCommand.action;

	for (let i = 0; i < target.length; i++){
		target[i].selected = true;
	}
}
function clickBtnEven(){
	const target = document.actionCommand.action;

	for (let i = 0; i < target.length; i++){
		if (i % 2 !== 0)
		{
			target[i].selected = true;
		}
		else
		{
			target[i].selected = false;
		}
	}
}
function clickBtnOdd(){
	const target = document.actionCommand.action;

	for (let i = 0; i < target.length; i++){
		if (i % 2 === 0)
		{
			target[i].selected = true;
		}
		else
		{
			target[i].selected = false;
		}
	}
}
</script>