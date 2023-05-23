using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Principal;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySqlConnector;
using static ace_access_system.Static_Class;
using MySqlX.XDevAPI.Relational;
using System.Diagnostics;
using System.Xml.Linq;

namespace ace_access_system
{
    public partial class Form_Permission : Form
    {
        private Address_book address_book = new Address_book();
        //判斷目前欄位是按下新建、修改、刪除
        private string currentOperation = "";
        //[變數]判斷目前radio事件所選值
        private string Status = "";
        //[布林]判斷按下確定或取消
        private bool shouldPerformOperation = false;

        public Form_Permission()
        {
            InitializeComponent();
            textBox_IDC.KeyPress += TextBoxHelper.Str_Keypress;

        }
        private void Fill_Area_info(ComboBox combobox)
        {
            MySqlCommand cmd_combo = new MySqlCommand("SELECT `Area` FROM `asc_access`.`area`", SQL_Conn.cn);
            combobox.Items.Clear();
            try
            {
                SQL_Conn.cn.Open();
                using (MySqlDataReader reader = cmd_combo.ExecuteReader())
                    while (reader.Read())
                    {
                        combobox.Items.Add(reader.GetString("Area"));
                    }
                SQL_Conn.cn.Close();
            }
            catch (Exception ex)
            {
                LogRecord.WriteLog(ex.Message, "form_permission");
            }
        }  //把Area資料填入區域combobox裡
        private void Form_Permission_Load(object sender, EventArgs e)
        {
            Renew();

        } //讀取介面時動作
        private void Renew()
        {
            button_add.Enabled = true;
            button_revise.Enabled = true;
            button_del.Enabled = true;
            button_export.Enabled = true;
            panel_Device.Enabled = false;
            panel_Device.BackColor = Color.LightBlue;
            panel_IP.Enabled = false;
            panel_IP.BackColor = Color.LightBlue;
            //numericUpDown_DoorNumC.Text = string.Empty;
            panel_check.Enabled = true;
            SQL_Conn.cn.Close();
            Fill_Area_info(comboBox_AreaC);
            try
            {
                string sql = "SELECT * From `asc_access`.`device_list`";
                MySqlCommand cmd = new MySqlCommand(sql, SQL_Conn.cn);
                SQL_Conn.cn.Open();
                MySqlDataReader reader = cmd.ExecuteReader();
                dataGridView_SQL.Rows.Clear();
                while (reader.Read())
                {
                    int index = this.dataGridView_SQL.Rows.Add();

                    this.dataGridView_SQL.Rows[index].Cells[0].Value = reader.GetInt32("dl_ID");
                    this.dataGridView_SQL.Rows[index].Cells[1].Value = reader.GetInt32("dl_Door");
                    this.dataGridView_SQL.Rows[index].Cells[2].Value = Way.GetWayName(reader.GetInt32("dl_Way"));
                    this.dataGridView_SQL.Rows[index].Cells[3].Value = reader.GetString("dl_Group");
                    this.dataGridView_SQL.Rows[index].Cells[4].Value = reader.GetString("dl_Name");
                    this.dataGridView_SQL.Rows[index].Cells[5].Value = EnableStatus.GetEnableStatus(reader.GetInt32("dl_Enable"));
                    this.dataGridView_SQL.Rows[index].Cells[6].Value = reader.GetString("dl_IP");
                    this.dataGridView_SQL.Rows[index].Cells[7].Value = reader.GetInt32("dl_Port");
                    object infoValue = reader.GetValue("dl_Info");
                    if (Convert.IsDBNull(infoValue))
                    {
                        this.dataGridView_SQL.Rows[index].Cells[8].Value = DBNull.Value;
                    }
                    else
                    {
                        this.dataGridView_SQL.Rows[index].Cells[8].Value = Convert.ToString(infoValue);
                    }
                }
                reader.Close();
                cmd.ExecuteNonQuery();
                SQL_Conn.cn.Close();
            }
            catch (MySql.Data.MySqlClient.MySqlException ex)
            {
                LogRecord.WriteLog(ex.Message, "form_permission");
            }
        } //更新介面

        private void button_add_Click(object sender, EventArgs e)
        {
            SQL_Conn.cn.Close();
            currentOperation = "Add";
            button_revise.Enabled = false;
            button_del.Enabled = false;
            button_export.Enabled = true;
            panel_Device.Enabled = true;
            panel_IP.Enabled = true;
            panel_check.Enabled = false;
            Clear_panel_info();
            Fill_Area_info(comboBox_Area);
            radioButton_On.Checked = true;

            MySqlCommand cmd = new MySqlCommand("SELECT max(`dl_ID`) FROM `asc_access`.`device_list`", SQL_Conn.cn);
            SQL_Conn.cn.Open();
            int maxid = Convert.ToInt32(cmd.ExecuteScalar());
            textBox_ID.Text = (maxid + 1).ToString();
            SQL_Conn.cn.Close();

        }//點擊新增按鈕事件
        private void Clear_panel_info()
        {
            textBox_IP.Text = string.Empty;
            numericUpDown_Port.Text = "60000";
            textBox_ID.Text = string.Empty;
            numericUpDown_DoorNum.Text = "1";
            comboBox_Way.Text = "雙向";
            comboBox_Area.Text = "區域1";
            listbox_Doors.Text = "";
            textBox_Info.Text = string.Empty;
            radioButton_On.Checked = false;
            radioButton_Off.Checked = false;
        } //清除ID&IP資料欄位
        private void button_revise_Click(object sender, EventArgs e)
        {
            currentOperation = "Revise";
            button_add.Enabled = false;
            button_del.Enabled = false;
            button_export.Enabled = true;
            panel_Device.Enabled = true;
            panel_IP.Enabled = true;
            panel_check.Enabled = false;
            Clear_panel_info();
            Fill_Area_info(comboBox_Area);
            Fill_panel_info();
        }//點擊修改按鈕事件

        private void button_del_Click(object sender, EventArgs e)
        {
            currentOperation = "Delete";
            button_add.Enabled = false;
            button_revise.Enabled = false;
            button_export.Enabled = false;
            panel_Device.Enabled = true;
            panel_Device.BackColor = Color.Red;
            panel_IP.Enabled = true;
            panel_IP.BackColor = Color.Red;
            panel_check.Enabled = false;
            Clear_panel_info();
            Fill_Area_info(comboBox_Area);
            Fill_panel_info();
        }//點擊刪除按鈕事件

        private void button_export_Click(object sender, EventArgs e)
        {
            try
            {
                DataTable dt = new();
                foreach (DataGridViewColumn col in dataGridView_SQL.Columns)
                {
                    dt.Columns.Add(col.HeaderText);
                }
                foreach (DataGridViewRow row in dataGridView_SQL.Rows)
                {
                    DataRow dr = dt.NewRow();
                    SQL_Conn.cn.Close();
                    for (int i = 0; i < row.Cells.Count; i++)
                    {
                        dr[i] = row.Cells[i].Value;
                    }

                    dt.Rows.Add(dr);
                }
                address_book.ExportToCsv(dt);
            }
            catch (Exception ex)
            {
                LogRecord.WriteLog(ex.Message, "form_permission");
            }
            SQL_Conn.cn.Close();
        }//導出csv

        private void button_close_Click(object sender, EventArgs e)
        {
            this.Close();
        }//離開當前視窗
        private void Fill_panel_info()
        {


            if (dataGridView_SQL.SelectedRows.Count > 0)
            {
                // 獲取所選擇行的值
                int selectedRowIndex = dataGridView_SQL.SelectedRows[0].Index;
                int selectedID = Convert.ToInt32(dataGridView_SQL.Rows[selectedRowIndex].Cells[0].Value);

                MySqlCommand cmd = new MySqlCommand("SELECT * FROM `asc_access`.`device_list` WHERE dl_ID = @dl_ID", SQL_Conn.cn);
                SQL_Conn.cn.Open();
                cmd.Parameters.AddWithValue("@dl_ID", selectedID);
                string dlGroup = "";
                string dlName = "";

                using (MySqlDataReader reader = cmd.ExecuteReader())
                {
                    if (reader.Read())
                    {
                        textBox_ID.Text = reader["dl_ID"].ToString();
                        numericUpDown_DoorNum.Text = reader["dl_Door"].ToString();
                        textBox_IP.Text = reader["dl_IP"].ToString();
                        numericUpDown_Port.Text = reader["dl_Port"].ToString();
                        textBox_Info.Text = reader["dl_Info"].ToString();

                        if (!reader.IsDBNull(reader.GetOrdinal("dl_Group")))
                        {
                            dlGroup = reader.GetString("dl_Group");
                        }
                        if (!reader.IsDBNull(reader.GetOrdinal("dl_Name")))
                        {
                            dlName = reader.GetString("dl_Name");
                            string[] doors = dlName.Split(',');
                            numericUpDown_DoorNum.Value = doors.Length;
                        }

                        if (reader["dl_Enable"] != DBNull.Value)
                        {
                            int enable = Convert.ToInt32(reader["dl_Enable"]);
                            if (enable == 1)
                            {
                                radioButton_On.Checked = true;
                            }
                            else if (enable == 0)
                            {
                                radioButton_Off.Checked = true;
                            }
                        }
                        else
                        {
                            radioButton_On.Checked = false;
                            radioButton_Off.Checked = false;
                        }
                        if (reader["dl_Way"] != DBNull.Value)
                        {
                            int group = Convert.ToInt32(reader["dl_Way"]);
                            if (group == 0)
                            {
                                comboBox_Way.Text = "關閉";
                            }
                            else if (group == 2)
                            {
                                comboBox_Way.Text = "只進";
                            }
                            else if (group == 3)
                            {
                                comboBox_Way.Text = "只出";
                            }
                        }
                        else
                        {
                            comboBox_Way.Text = "雙向";
                        }
                        comboBox_Area.Text = dlGroup;
                        listbox_Doors.Text = dlName;
                        

                    }
                    SQL_Conn.cn.Close();
                }
            }

        } //將在Gridview選取行(預設只能選一行)資料帶入到panel_info的項目內

        private void button_enter_Click(object sender, EventArgs e) //按下確定
        {
            if (currentOperation == "Add")
            {
                DialogResult add_result = MessageBox.Show("您確定要新增嗎?", "確定新增", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    shouldPerformOperation = true;

                    MySqlCommand cmd = new MySqlCommand();
                    string str = "INSERT INTO `asc_access`.`device_list` (dl_ID, dl_Door, dl_Way, dl_Group, dl_Name, dl_Enable, dl_IP, dl_Port, dl_Info) " +
                                    "VALUES (@dl_ID, @dl_Door, @dl_Way, @dl_Group, @dl_Name, @dl_Enable, @dl_IP, @dl_Port, @dl_Info)";
                    int way;
                    if (comboBox_Way.Text == "雙向") { way = 1; }
                    else if (comboBox_Way.Text == "關閉") { way = 0; }
                    else if (comboBox_Way.Text == "只進") { way = 2; }
                    else if (comboBox_Way.Text == "只出") { way = 3; }
                    else { way = 1; }
                    int enable;
                    if (radioButton_On.Checked == true) { enable = 1; }
                    else if (radioButton_Off.Checked == true) { enable = 0; }
                    else { enable = 2; }
                    cmd.Parameters.AddWithValue("@dl_ID", Convert.ToInt32(textBox_ID.Text));
                    cmd.Parameters.AddWithValue("@dl_Door", Convert.ToInt32(numericUpDown_DoorNum.Text));
                    cmd.Parameters.AddWithValue("@dl_Way", way);
                    cmd.Parameters.AddWithValue("@dl_Group", comboBox_Area.Text);
                    string selectedDoors = String.Join(",", listbox_Doors.Items.Cast<string>().ToArray());
                    cmd.Parameters.AddWithValue("@dl_Name", selectedDoors);
                    cmd.Parameters.AddWithValue("@dl_Enable", enable);
                    cmd.Parameters.AddWithValue("@dl_IP", textBox_IP.Text);
                    cmd.Parameters.AddWithValue("@dl_Port", numericUpDown_Port.Text);
                    cmd.Parameters.AddWithValue("@dl_Info", textBox_Info.Text);
                    cmd.CommandText = str;
                    cmd.Connection = SQL_Conn.cn;
                    SQL_Conn.cn.Open();
                    //一些輸入判定
                    if (string.IsNullOrEmpty(numericUpDown_DoorNum.Value.ToString())) { MessageBox.Show("請輸入門數量"); SQL_Conn.cn.Close(); return; }
                    else if (string.IsNullOrEmpty(textBox_IP.Text)) { MessageBox.Show("請輸入IP位址"); SQL_Conn.cn.Close(); return; }
                    else if (string.IsNullOrEmpty(numericUpDown_Port.Text)) { MessageBox.Show("請輸入Port"); SQL_Conn.cn.Close(); return; }
                    else
                    {
                        int rowsAffected = cmd.ExecuteNonQuery();
                        if (rowsAffected > 0)
                        {
                            MessageBox.Show("新增成功");
                        }
                        else
                        {
                            MessageBox.Show("新增失敗");
                        }
                        Clear_panel_info();
                        SQL_Conn.cn.Close();
                        Renew();
                    }
                }
                else
                {
                    shouldPerformOperation = false;
                }

            } //"新增"的程式碼
            else if (currentOperation == "Revise")
            {
                DialogResult add_result = MessageBox.Show("您確定要修改嗎?", "確定修改", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    shouldPerformOperation = true;

                    if (dataGridView_SQL.SelectedRows.Count > 0)
                    {
                        // 獲取所選擇行的值
                        int selectedRowIndex = dataGridView_SQL.SelectedRows[0].Index;
                        int selectedID = Convert.ToInt32(dataGridView_SQL.Rows[selectedRowIndex].Cells[0].Value);
                        MySqlCommand cmd = new MySqlCommand("UPDATE `asc_access`.`device_list` SET `dl_ID`=@dl_ID, `dl_Door`=@dl_Door, `dl_Way`=@dl_Way, `dl_Group`=@dl_Group, `dl_Name`=@dl_Name, `dl_Enable`=@dl_Enable, " +
                                                             "`dl_IP`=@dl_IP, `dl_Port`=@dl_Port, `dl_Info`=@dl_Info WHERE `dl_ID`=@dl_ID", SQL_Conn.cn);
                        SQL_Conn.cn.Open();
                        int way;
                        if (comboBox_Way.Text == "雙向") { way = 1; }
                        else if (comboBox_Way.Text == "關閉") { way = 0; }
                        else if (comboBox_Way.Text == "只進") { way = 2; }
                        else if (comboBox_Way.Text == "只出") { way = 3; }
                        else { way = 1; }
                        int enable;
                        if (radioButton_On.Checked == true) { enable = 1; }
                        else if (radioButton_Off.Checked == true) { enable = 0; }
                        else { enable = 2; }
                        cmd.Parameters.AddWithValue("@dl_ID", Convert.ToInt32(textBox_ID.Text));
                        cmd.Parameters.AddWithValue("@dl_Door", Convert.ToInt32(numericUpDown_DoorNum.Text));
                        cmd.Parameters.AddWithValue("@dl_Way", way);
                        cmd.Parameters.AddWithValue("@dl_Group", comboBox_Area.Text);
                        string selectedDoors = String.Join(",", listbox_Doors.Items.Cast<string>().ToArray());
                        cmd.Parameters.AddWithValue("@dl_Name", selectedDoors);
                        cmd.Parameters.AddWithValue("@dl_Enable", enable);
                        cmd.Parameters.AddWithValue("@dl_IP", textBox_IP.Text);
                        cmd.Parameters.AddWithValue("@dl_Port", numericUpDown_Port.Text);
                        cmd.Parameters.AddWithValue("@dl_Info", textBox_Info.Text);

                        if (string.IsNullOrEmpty(numericUpDown_DoorNum.Value.ToString())) { MessageBox.Show("請輸入門數量"); SQL_Conn.cn.Close(); return; }
                        else if (string.IsNullOrEmpty(textBox_IP.Text)) { MessageBox.Show("請輸入IP位址"); SQL_Conn.cn.Close(); return; }
                        else if (string.IsNullOrEmpty(numericUpDown_Port.Text)) { MessageBox.Show("請輸入Port"); SQL_Conn.cn.Close(); return; }
                        else
                        {
                            int rowsAffected = cmd.ExecuteNonQuery();
                            if (rowsAffected > 0)
                            {
                                MessageBox.Show("修改成功");
                                //Trace.WriteLine($"enable = {enable}");
                            }
                            else
                            {
                                MessageBox.Show("修改失敗");
                            }
                        }
                        SQL_Conn.cn.Close();
                        Renew();
                    }
                }
                else
                {
                    shouldPerformOperation = false;
                }
            }//修改的程式碼
            else if (currentOperation == "Delete")
            {
                DialogResult add_result = MessageBox.Show("您確定要刪除嗎?", "確定刪除", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    if (dataGridView_SQL.SelectedRows.Count > 0)
                    {
                        int selectedRowIndex = dataGridView_SQL.SelectedRows[0].Index;
                        int selectedID = Convert.ToInt32(dataGridView_SQL.Rows[selectedRowIndex].Cells[0].Value);

                        MySqlCommand del_cmd = new MySqlCommand("DELETE FROM `asc_access`.`device_list` WHERE dl_ID = @dl_ID", SQL_Conn.cn);

                        SQL_Conn.cn.Open();
                        del_cmd.Parameters.AddWithValue("@dl_ID", selectedID);
                        //del_cmd.ExecuteNonQuery();
                        int rowsAffected = del_cmd.ExecuteNonQuery();

                        if (rowsAffected > 0)
                        {
                            MessageBox.Show("刪除成功！");
                            Renew();
                        }
                        else
                        {
                            MessageBox.Show("刪除失敗！");
                        }
                    }
                    else
                    {
                        MessageBox.Show("請先選擇要刪除的行！");
                    }
                }
                SQL_Conn.cn.Close();
            }//刪除的程式碼
        }
        private void button_cancel_Click(object sender, EventArgs e)
        {
            if (currentOperation == "Add")
            {
                //取消新增:清除panel_info上已填選資料;返回Form_member介面
                DialogResult add_result = MessageBox.Show("您確定要取消新增嗎?", "取消新增", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    shouldPerformOperation = true;
                    Clear_panel_info();
                    Renew();
                }
                else
                {
                    shouldPerformOperation = false;

                }

            }
            else if (currentOperation == "Revise")
            {
                DialogResult add_result = MessageBox.Show("您確定要取消修改嗎?", "取消修改", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    shouldPerformOperation = true;
                    Clear_panel_info();
                    Renew();
                }
                else
                {
                    shouldPerformOperation = false;

                }
            }
            else if (currentOperation == "Delete")
            {
                DialogResult add_result = MessageBox.Show("不刪除嗎?", "取消刪除", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    shouldPerformOperation = true;
                    Clear_panel_info();
                    Renew();
                }
                else
                {
                    shouldPerformOperation = false;

                }
            }
        } //按下取消

        private void button_Area_Manage_Click(object sender, EventArgs e)
        {
            Form_AreaManage mForm_AreaManage = new();
            mForm_AreaManage.Show();
        } //控制器區域管理

        private void comboBox_Area_SelectedIndexChanged(object sender, EventArgs e)
        {
            SQL_Conn.cn.Close();
            // 清空 ListBox
            listbox_Doors.Items.Clear();

            // 取得選擇的 Area
            string? selectedArea = comboBox_Area.SelectedItem.ToString();

            // 建立 SQL 查詢
            string query = $"SELECT `Doors` FROM `asc_access`.`area` WHERE `Area` = '{selectedArea}'";

            using (MySqlCommand command = new MySqlCommand(query, SQL_Conn.cn))
            {
                SQL_Conn.cn.Open();
                using (MySqlDataReader reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        // 將 Doors 欄位中的每一個項目加入 ListBox 的不同行
                        string doorsString = reader.GetString(0);
                        string[] doors = doorsString.Split(',');
                        foreach (string door in doors)
                        {
                            listbox_Doors.Items.Add(door);
                        }
                    }
                }
                SQL_Conn.cn.Close();
            }

        } //選區域時自動帶入門ID

        private void button_check_Click(object sender, EventArgs e)
        {
            // 搜尋條件去頭尾空白
            string IDC = textBox_IDC.Text.Trim();
            string DoorNumC = numericUpDown_DoorNumC.Text.Trim();
            string WayC = comboBox_WayC.Text.Trim();
            string AreaC = comboBox_AreaC.Text.Trim();
            int enableC;
            if (radioButton_OnC.Checked == true) { enableC = 1; }
            else if (radioButton_OffC.Checked == true) { enableC = 0; }
            else { enableC = 2; }

            // 編寫模糊查詢的SQL語句
            string query = "SELECT * FROM `asc_access`.`device_list` WHERE 1=1";

            if (!string.IsNullOrWhiteSpace(textBox_IDC.Text))
            {
                query += $" AND dl_ID LIKE '%{textBox_IDC.Text}%'";
            }
            if (!string.IsNullOrWhiteSpace(numericUpDown_DoorNumC.Text))
            {
                query += $" AND dl_Door LIKE '%{numericUpDown_DoorNumC.Text}%'";
            }
            if (!string.IsNullOrWhiteSpace(comboBox_WayC.Text))
            {
                int wayCode = Way.GetWayCode(comboBox_WayC.Text);
                query += $" AND dl_Way LIKE '%{wayCode}%'";
            }
            if (!string.IsNullOrWhiteSpace(comboBox_AreaC.Text))
            {
                query += $" AND dl_Group LIKE '%{comboBox_AreaC.Text}%'";
            }
            if (!string.IsNullOrWhiteSpace(enableC.ToString()))
            {
                query += $" AND dl_Enable LIKE '%{enableC}%'";
            }
            //如果欄位不是空值就把輸入值加到command裡
            {
                MySqlCommand cmd = new MySqlCommand(query, SQL_Conn.cn);
                SQL_Conn.cn.Open();
                if (!string.IsNullOrEmpty(IDC)) { cmd.Parameters.AddWithValue("@dl_ID", IDC); }
                if (!string.IsNullOrEmpty(DoorNumC)) { cmd.Parameters.AddWithValue("@dl_Door", DoorNumC); }
                if (!string.IsNullOrEmpty(WayC)) { cmd.Parameters.AddWithValue("@dl_Way", WayC); }
                if (!string.IsNullOrEmpty(AreaC)) { cmd.Parameters.AddWithValue("@dl_Group", AreaC); }
                if (!string.IsNullOrEmpty(enableC.ToString())) { cmd.Parameters.AddWithValue("@dl_Enable", enableC); }

                MySqlDataReader reader = cmd.ExecuteReader();
                dataGridView_SQL.Rows.Clear(); //清掉原本的顯示資料
                while (reader.Read())
                {
                    int index = this.dataGridView_SQL.Rows.Add();

                    this.dataGridView_SQL.Rows[index].Cells[0].Value = reader.GetInt32("dl_ID");
                    this.dataGridView_SQL.Rows[index].Cells[1].Value = reader.GetInt32("dl_Door");
                    this.dataGridView_SQL.Rows[index].Cells[2].Value = Way.GetWayName(reader.GetInt32("dl_Way"));
                    this.dataGridView_SQL.Rows[index].Cells[3].Value = reader.GetString("dl_Group");
                    this.dataGridView_SQL.Rows[index].Cells[4].Value = reader.GetString("dl_Name");
                    this.dataGridView_SQL.Rows[index].Cells[5].Value = EnableStatus.GetEnableStatus(reader.GetInt32("dl_Enable"));
                    this.dataGridView_SQL.Rows[index].Cells[6].Value = reader.GetString("dl_IP");
                    this.dataGridView_SQL.Rows[index].Cells[7].Value = reader.GetInt32("dl_Port");
                    this.dataGridView_SQL.Rows[index].Cells[8].Value = reader.GetString("dl_Info");
                }
                reader.Close();
                cmd.ExecuteNonQuery();
                SQL_Conn.cn.Close();
            }
        }
        private void button_ClearC_Click(object sender, EventArgs e)
        {
            textBox_IDC.Text = string.Empty;
            numericUpDown_DoorNumC.Text = string.Empty;
            comboBox_WayC.Text = string.Empty;
            comboBox_AreaC.Text = string.Empty;
        }//清除填選在查詢欄位資料

        private void button1_Click(object sender, EventArgs e)
        {
            Renew();
        }
    }
}
