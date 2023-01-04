
% rebase('layout.tpl', title='千手九龍', year=year)

hello

<div class="flexcontainer">
	<div class="flexitem item1">
		<form action="./top">
			<button type="submit">Top</button>
		</form>
		<br />
		<form action="./allCreate" method="post">
			<button type="submit">allCreate</button>
		</form>
		<br />
		<form action="./allDrop" method="post">
			<button type="submit">allDrop</button>
		</form>
		<br />
		<form action="./createCharaAndSpeedUp" method="post">
			<label>Id</label>
			<input type="text" name="user_id">
			<br />
			<label>Password</label>
			<input type="password" name="user_password">
			<br />
			<button type="submit">作成及び加速</button>
		</form>
		<br />
		<details>
			<summary>
				User
			</summary>
			<form action="./createTableUser" method="post">
				<button type="submit">createTableUser</button>
			</form>
			<form action="./dropTableUser" method="post">
				<button type="submit">dropTableUser</button>
			</form>
		</details>
		<details>
			<summary>
				ChatLogs
			</summary>
			<form action="./createTableChatLogs" method="post">
				<button type="submit">createTableChatLogs</button>
			</form>
			<form action="./dropTableChatLogs" method="post">
				<button type="submit">dropTableChatLogs</button>
			</form>
		</details>
		<details>
			<summary>
			Map
			</summary>
			<form action="./createTableMap" method="post">
				<button type="submit">createTableMap</button>
			</form>
			<form action="./dropTableMap" method="post">
				<button type="submit">dropTableMap</button>
			</form>
			<form action="./insertTableMap" method="post">
				<button type="submit">insertTableMap</button>
			</form>
		</details>
		<details>
			<summary>
			MST
			</summary>
			<form action="./createTableMST" method="post">
				<button type="submit">createTableMST</button>
			</form>
			<form action="./dropTableMST" method="post">
				<button type="submit">dropTableMST</button>
			</form>
			<form action="./insertTableMST" method="post">
				<button type="submit">insertTableMST</button>
			</form>
		</details>
		<details>
			<summary>
			News
			</summary>
			<form action="./createTableNews" method="post">
				<button type="submit">createTableNews</button>
			</form>
			<form action="./dropTableNews" method="post">
				<button type="submit">dropTableNews</button>
			</form>
		</details>
		<details>
			<summary>
			Action
			</summary>
			<form action="./createTableAction" method="post">
				<button type="submit">createTableAction</button>
			</form>
			<form action="./dropTableAction" method="post">
				<button type="submit">dropTableAction</button>
			</form>
		</details>
		<details>
			<summary>
			ActionLogs
			</summary>
			<form action="./createTableActionLogs" method="post">
				<button type="submit">createTableActionLogs</button>
			</form>
			<form action="./dropTableActionLogs" method="post">
				<button type="submit">dropTableActionLogs</button>
			</form>
		</details>
		<details>
			<summary>
			TableTime
			</summary>
			<form action="./createTableTime" method="post">
				<button type="submit">createTableTime</button>
			</form>
			<form action="./dropTableTime" method="post">
				<button type="submit">dropTableTime</button>
			</form>
			<form action="./insertTableTime" method="post">
				<button type="submit">insertTableTime</button>
			</form>
		</details>
		<details>
			<summary>
			Soldier
			</summary>
			<form action="./createSoldier" method="post">
				<button type="submit">createSoldier</button>
			</form>
			<form action="./dropSoldier" method="post">
				<button type="submit">dropSoldier</button>
			</form>
			<form action="./insertSoldier" method="post">
				<button type="submit">insertSoldier</button>
			</form>
		</details>
		<details>
			<summary>
			SoldierPersonal
			</summary>
			<form action="./createSoldierPersonal" method="post">
				<button type="submit">createSoldierPersonal</button>
			</form>
			<form action="./dropSoldierPersonal" method="post">
				<button type="submit">dropSoldierPersonal</button>
			</form>
		</details>
		<details>
			<summary>
			ManageQuest
			</summary>
			<form action="./createManageQuest" method="post">
				<button type="submit">createManageQuest</button>
			</form>
			<form action="./dropManageQuest" method="post">
				<button type="submit">dropManageQuest</button>
			</form>
		</details>
		<details>
			<summary>
			MeetingRoom
			</summary>
			<form action="./createMeetingRoom" method="post">
				<button type="submit">createMeetingRoom</button>
			</form>
			<form action="./dropMeetingRoom" method="post">
				<button type="submit">dropMeetingRoom</button>
			</form>
		</details>
		<br />
	</div>
</div>