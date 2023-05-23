using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySqlConnector;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using static ace_access_system.Static_Class;

namespace ace_access_system
{
    public partial class Form_AreaManage : Form
    {
        public Form_AreaManage()
        {
            InitializeComponent();
        }

        private void Form_AreaManage_Load(object sender, EventArgs e)
        {
            Renew();
        }
        private void Renew()
        {
            SQL_Conn.cn.Close();
            // 清空樹狀圖
            treeView_Area.Nodes.Clear();

            // 從 MySQL 資料庫讀取資料
            DataTable dt = new DataTable();
            MySqlDataAdapter da = new MySqlDataAdapter("SELECT * FROM asc_access.area", SQL_Conn.cn);
            da.Fill(dt);

            // 加入到樹狀圖的根節點中
            foreach (DataRow row in dt.Rows)
            {
                // 新增根節點
                string areaName = row["Area"].ToString();
                TreeNode rootNode = new TreeNode(areaName);
                //rootNode.Tag = row["AreaId"].ToString();

                // 將子節點分割成陣列
                string[] doors = row["Doors"].ToString().Split(',');

                // 加入到樹狀圖的根節點下面
                foreach (string door in doors)
                {
                    if (!string.IsNullOrWhiteSpace(door))
                    {
                        TreeNode node = new TreeNode(door);
                        rootNode.Nodes.Add(node);
                    }
                }

                // 新增根節點
                treeView_Area.Nodes.Add(rootNode);
            }
        }
        private void button_Upper_add_Click(object sender, EventArgs e)
        {
            SQL_Conn.cn.Close();
            string areaName = textBox_Upper.Text;
            if (!string.IsNullOrEmpty(areaName))
            {
                // 在 treeView_Area 中建立一個新的根節點
                TreeNode rootNode = new TreeNode(areaName);
                treeView_Area.Nodes.Add(rootNode);

                //加進MySQL資料表中
                MySqlCommand cmd = new MySqlCommand("INSERT INTO `asc_access`.`area` (Area) VALUES (@area)", SQL_Conn.cn);
                cmd.Parameters.AddWithValue("@area", areaName);
                SQL_Conn.cn.Open();
                int result = cmd.ExecuteNonQuery();
                if (result < 0)
                {
                    MessageBox.Show("插入失敗");
                }
            }
            else
            {
                MessageBox.Show("請輸入根目錄名稱");
            }
            SQL_Conn.cn.Close();
            Renew();
        }//建立根目錄

        private void button_Lower_Add_Click(object sender, EventArgs e)
        {
            SQL_Conn.cn.Close();
            string newChildName = textBox_Lower.Text.Trim();
            if (string.IsNullOrEmpty(newChildName)) // 檢查是否輸入了有效的子節點名稱
            {
                MessageBox.Show("請輸入名稱");
                return;
            }
            TreeNode selectedNode = treeView_Area.SelectedNode;
            if (selectedNode == null) // 檢查是否已選定目標
            {
                MessageBox.Show("請先選擇目標");
                return;
            }
            TreeNode newChildNode = selectedNode.Nodes.Add(newChildName); // 建立新的子節點
            string parentNodeName = selectedNode.Text;
            // 將新名稱插入到目標的子節點中並更新 MySQL 資料庫
            try
            {

                MySqlCommand cmd = new MySqlCommand($"UPDATE area SET Doors = CONCAT_WS(',', Doors, '{newChildName}') WHERE Area = '{parentNodeName}'", SQL_Conn.cn);
                /*
                CONCAT_WS 的作用是將新的子目錄名稱和已有的子目錄名稱連接在一起，以逗號作為分隔符。
                這樣做的目的是為了讓每個父目錄的 Doors 欄位中存儲多個子目錄名稱，方便後續的查詢和顯示。
                */
                SQL_Conn.cn.Open();
                int rowsAffected = cmd.ExecuteNonQuery();
                if (rowsAffected == 0)
                {
                    MessageBox.Show("操作失敗");
                }

            }
            catch (Exception ex)
            {
                MessageBox.Show($"操作失敗: {ex.Message}");
            }
            Renew();
        }//加入子目錄

        private void button_Del_Click(object sender, EventArgs e)
        {
            TreeNode selectedNode = treeView_Area.SelectedNode;
            
            if (selectedNode != null)
            {
                if (selectedNode.Parent == null) // 刪除根節點及其下的所有子節點
                {
                    if (MessageBox.Show("確定要刪除嗎？", "刪除", MessageBoxButtons.YesNo) == DialogResult.Yes)
                    {
                        // 刪除節點及其子節點
                        selectedNode.Remove();

                        // 刪除 MySQL 資料庫中相應的紀錄
                        string deleteQuery = "DELETE FROM `asc_access`.`area` WHERE Area=@areaName OR Area LIKE @areaNameChild ESCAPE '/'";
                        MySqlCommand cmd = new MySqlCommand(deleteQuery, SQL_Conn.cn);
                        cmd.Parameters.AddWithValue("@areaName", selectedNode.Text);
                        cmd.Parameters.AddWithValue("@areaNameChild", selectedNode.Text + "/%");
                        SQL_Conn.cn.Open();
                        int result = cmd.ExecuteNonQuery();
                        if (result < 0)
                        {
                            MessageBox.Show("刪除失敗");
                        }
                        SQL_Conn.cn.Close();
                    }
                }
                else // 刪除子節點
                {
                    if (selectedNode.Parent.Nodes.Count == 1)
                    {
                        MessageBox.Show("已經是最後一個節點，無法刪除。");
                        return;
                    }

                    if (MessageBox.Show("確定要刪除嗎？", "刪除", MessageBoxButtons.YesNo) == DialogResult.Yes)
                    {

                        // 更新 MySQL 資料庫中相應的紀錄
                        string nodeId = treeView_Area.SelectedNode.Text;
                        string parentId = treeView_Area.SelectedNode.Parent.Text;
                        if (nodeId == null || parentId == null)
                        {
                            MessageBox.Show("選擇無效節點");
                            return;
                        }
                        string query = "UPDATE `asc_access`.`area` SET `Doors` = TRIM(BOTH ',' FROM REPLACE(CONCAT(',', `Doors`, ','), CONCAT(',', @nodeId, ','), ',')) WHERE `Area` = @parentId";


                        MySqlCommand cmd = new MySqlCommand(query, SQL_Conn.cn);
                        cmd.Parameters.AddWithValue("@nodeId", nodeId);
                        cmd.Parameters.AddWithValue("@parentId", parentId);
                        Debug.WriteLine(cmd.CommandText);
                        Debug.WriteLine(nodeId);
                        Debug.WriteLine(parentId);
                        SQL_Conn.cn.Open();
                        int result = cmd.ExecuteNonQuery();
                        if (result < 0)
                        {
                            MessageBox.Show("刪除失敗");
                        }
                        SQL_Conn.cn.Close();
                    }
                }
            }
            Renew();
        }//刪除跟目錄或子節點


        private void button_Revise_Click(object sender, EventArgs e)
        {
            TreeNode selectedNode = treeView_Area.SelectedNode;
            string SNodeName = selectedNode.Text;
            string newName = textBox_Target.Text;
            if (selectedNode != null)
            {
                //string oldName = selectedNode.Text;
                // 更新節點名稱
                // selectedNode.Text = newName;
                textBox_Target.Text = newName;

                // 更新MySQL資料庫中對應的名稱
                MySqlCommand cmd;

                if (selectedNode.Parent == null)
                {
                    // 更新區域名稱
                    cmd = new MySqlCommand("UPDATE asc_access.area SET Area=@newName WHERE Area=@oldName", SQL_Conn.cn);
                    cmd.Parameters.AddWithValue("@oldName", SNodeName);
                    cmd.Parameters.AddWithValue("@newName", newName);
                    Debug.WriteLine("selectedNode", SNodeName);
                }
                else
                {
                    /*
                    // 更新門名稱
                    string rootName = selectedNode.Parent.Text;
                    cmd = new MySqlCommand("UPDATE asc_access.area SET Doors=@newName WHERE Area=@rootName AND Doors=@oldName", SQL_Conn.cn);
                    cmd.Parameters.AddWithValue("@rootName", rootName);
                    cmd.Parameters.AddWithValue("@oldName", parentNodeName);
                    cmd.Parameters.AddWithValue("@newName", newName);
                    Debug.WriteLine(cmd.CommandText);
                    Debug.WriteLine("rootName", rootName);
                    */
                    // 更新 MySQL 資料庫中相應的紀錄
                    string nodeId = SNodeName;
                    string parentId = treeView_Area.SelectedNode.Parent.Text;
                    if (nodeId == null || parentId == null)
                    {
                        MessageBox.Show("選擇無效節點");
                        return;
                    }
                    cmd = new MySqlCommand("UPDATE `asc_access`.`area` SET `Doors` = TRIM(BOTH ',' FROM REPLACE(CONCAT(',', `Doors`, ','), CONCAT(',', @oldDoor, ','), CONCAT(',', @newDoor, ','))) WHERE `Area` = @parentId ", SQL_Conn.cn);
                    cmd.Parameters.AddWithValue("@oldDoor", SNodeName);
                    cmd.Parameters.AddWithValue("@newDoor", newName);
                    cmd.Parameters.AddWithValue("@parentId", parentId);

                }
                SQL_Conn.cn.Open();
                int result = cmd.ExecuteNonQuery();
                SQL_Conn.cn.Close();
                if (result < 0)
                {
                    MessageBox.Show("更新失敗");
                }
            }
            else 
            {
                MessageBox.Show("請選擇欲修改目標");
            }
            Renew();
        }//修改名稱部分

        private void treeView_Area_AfterSelect(object sender, TreeViewEventArgs e)
        {
            if (e.Node == null)
            {
                return; // 如果 e.Node 為 null，則直接返回
            }
            TreeNode selectedNode = treeView_Area.SelectedNode;
            if (selectedNode == null)
            {
                return; // 如果 selectedNode 為 null，則直接返回
            }
            string targetName = selectedNode.Text;
            if (string.IsNullOrEmpty(targetName)) // 如果 targetName 為空或為 null，則顯示錯誤訊息並返回
            {
                MessageBox.Show("未選擇目標");
                return;
            }
            selectedNode.Checked = true; // 保持目標的選定狀態
            textBox_Target.Text = targetName;
        }//選定樹狀圖中目標
    }
}
