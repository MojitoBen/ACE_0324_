namespace ace_access_system
{
    partial class Form_AreaManage
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form_AreaManage));
            panel2 = new Panel();
            textBox_Target = new TextBox();
            button_Revise = new Button();
            label_input = new Label();
            panel1 = new Panel();
            label2 = new Label();
            textBox_Lower = new TextBox();
            textBox_Upper = new TextBox();
            label1 = new Label();
            button_Del = new Button();
            button_Lower_Add = new Button();
            button_Upper_add = new Button();
            treeView_Area = new TreeView();
            panel2.SuspendLayout();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel2
            // 
            panel2.BackColor = Color.LightBlue;
            panel2.Controls.Add(textBox_Target);
            panel2.Controls.Add(button_Revise);
            panel2.Controls.Add(label_input);
            panel2.Location = new Point(2, 1);
            panel2.Name = "panel2";
            panel2.Size = new Size(443, 65);
            panel2.TabIndex = 3;
            // 
            // textBox_Target
            // 
            textBox_Target.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            textBox_Target.Location = new Point(101, 17);
            textBox_Target.Name = "textBox_Target";
            textBox_Target.Size = new Size(205, 29);
            textBox_Target.TabIndex = 2;
            // 
            // button_Revise
            // 
            button_Revise.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button_Revise.ImageAlign = ContentAlignment.BottomCenter;
            button_Revise.Location = new Point(312, 8);
            button_Revise.Name = "button_Revise";
            button_Revise.Size = new Size(116, 45);
            button_Revise.TabIndex = 2;
            button_Revise.Text = "修改區域名稱";
            button_Revise.UseVisualStyleBackColor = true;
            button_Revise.Click += button_Revise_Click;
            // 
            // label_input
            // 
            label_input.AutoSize = true;
            label_input.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label_input.Location = new Point(10, 23);
            label_input.Name = "label_input";
            label_input.Size = new Size(90, 21);
            label_input.TabIndex = 1;
            label_input.Text = "已選定區域";
            // 
            // panel1
            // 
            panel1.BackColor = Color.LightBlue;
            panel1.Controls.Add(label2);
            panel1.Controls.Add(textBox_Lower);
            panel1.Controls.Add(textBox_Upper);
            panel1.Controls.Add(label1);
            panel1.Controls.Add(button_Del);
            panel1.Controls.Add(button_Lower_Add);
            panel1.Controls.Add(button_Upper_add);
            panel1.Location = new Point(2, 60);
            panel1.Name = "panel1";
            panel1.Size = new Size(443, 503);
            panel1.TabIndex = 2;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label2.Location = new Point(21, 237);
            label2.Name = "label2";
            label2.Size = new Size(74, 21);
            label2.TabIndex = 6;
            label2.Text = "次級區域";
            // 
            // textBox_Lower
            // 
            textBox_Lower.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            textBox_Lower.Location = new Point(101, 234);
            textBox_Lower.Name = "textBox_Lower";
            textBox_Lower.Size = new Size(205, 29);
            textBox_Lower.TabIndex = 5;
            // 
            // textBox_Upper
            // 
            textBox_Upper.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            textBox_Upper.Location = new Point(101, 47);
            textBox_Upper.Name = "textBox_Upper";
            textBox_Upper.Size = new Size(205, 29);
            textBox_Upper.TabIndex = 3;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label1.Location = new Point(10, 50);
            label1.Name = "label1";
            label1.Size = new Size(90, 21);
            label1.TabIndex = 4;
            label1.Text = "最高級區域";
            // 
            // button_Del
            // 
            button_Del.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button_Del.Image = (Image)resources.GetObject("button_Del.Image");
            button_Del.ImageAlign = ContentAlignment.BottomCenter;
            button_Del.Location = new Point(101, 404);
            button_Del.Name = "button_Del";
            button_Del.Size = new Size(205, 76);
            button_Del.TabIndex = 3;
            button_Del.Text = "刪除選定區域";
            button_Del.TextAlign = ContentAlignment.BottomCenter;
            button_Del.UseVisualStyleBackColor = true;
            button_Del.Click += button_Del_Click;
            // 
            // button_Lower_Add
            // 
            button_Lower_Add.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button_Lower_Add.Image = (Image)resources.GetObject("button_Lower_Add.Image");
            button_Lower_Add.ImageAlign = ContentAlignment.BottomCenter;
            button_Lower_Add.Location = new Point(101, 282);
            button_Lower_Add.Name = "button_Lower_Add";
            button_Lower_Add.Size = new Size(205, 76);
            button_Lower_Add.TabIndex = 1;
            button_Lower_Add.Text = "增加次級區域";
            button_Lower_Add.TextAlign = ContentAlignment.BottomCenter;
            button_Lower_Add.UseVisualStyleBackColor = true;
            button_Lower_Add.Click += button_Lower_Add_Click;
            // 
            // button_Upper_add
            // 
            button_Upper_add.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button_Upper_add.Image = (Image)resources.GetObject("button_Upper_add.Image");
            button_Upper_add.ImageAlign = ContentAlignment.BottomCenter;
            button_Upper_add.Location = new Point(101, 99);
            button_Upper_add.Name = "button_Upper_add";
            button_Upper_add.Size = new Size(205, 76);
            button_Upper_add.TabIndex = 0;
            button_Upper_add.Text = "增加最高級區域";
            button_Upper_add.TextAlign = ContentAlignment.BottomCenter;
            button_Upper_add.UseVisualStyleBackColor = true;
            button_Upper_add.Click += button_Upper_add_Click;
            // 
            // treeView_Area
            // 
            treeView_Area.Location = new Point(436, 1);
            treeView_Area.Name = "treeView_Area";
            treeView_Area.Size = new Size(546, 562);
            treeView_Area.TabIndex = 4;
            treeView_Area.AfterSelect += treeView_Area_AfterSelect;
            // 
            // Form_AreaManage
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(984, 561);
            Controls.Add(treeView_Area);
            Controls.Add(panel1);
            Controls.Add(panel2);
            Name = "Form_AreaManage";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "控制器區域管理";
            Load += Form_AreaManage_Load;
            panel2.ResumeLayout(false);
            panel2.PerformLayout();
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel2;
        private TextBox textBox_Target;
        private Button button_Revise;
        private Label label_input;
        private Panel panel1;
        private Button button_Del;
        private Button button_Lower_Add;
        private Button button_Upper_add;
        private TreeView treeView_Area;
        private Label label1;
        private Label label2;
        private TextBox textBox_Lower;
        private TextBox textBox_Upper;
    }
}