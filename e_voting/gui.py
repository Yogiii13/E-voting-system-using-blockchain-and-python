import json
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk

from .blockchain import Blockchain


class BlockchainGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Secure Blockchain Voting")
        self.master.geometry("950x650")
        self.master.resizable(False, False)
        self.master.configure(bg="#f3f6fb")

        self.blockchain = Blockchain()
        self.voter_id_var = tk.StringVar()
        self.selected_candidate = tk.StringVar()
        self.constituency = None

        self.create_styles()
        self.create_widgets()
        self.voter_id_var.trace_add("write", self.on_voter_id_change)

    def create_styles(self):
        style = ttk.Style(self.master)
        style.theme_use("clam")
        style.configure("Header.TLabel", background="#34495e", foreground="#ffffff", font=("Segoe UI", 20, "bold"))
        style.configure("Section.TLabel", background="#f3f6fb", foreground="#2c3e50", font=("Segoe UI", 12, "bold"))
        style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=8)
        style.configure("TEntry", font=("Segoe UI", 11))
        style.configure("TRadiobutton", background="#f3f6fb", font=("Segoe UI", 11))
        style.configure("Info.TLabel", background="#f3f6fb", foreground="#34495e")
        style.map("TButton", background=[("active", "#5d8aa8")])

    def create_widgets(self):
        header_frame = ttk.Frame(self.master, padding=(20, 20), style="Card.TFrame")
        header_frame.pack(fill="x")

        header_label = ttk.Label(header_frame, text="Secure Blockchain Voting", style="Header.TLabel")
        header_label.pack(anchor="center")

        main_frame = ttk.Frame(self.master, padding=(20, 10), style="Card.TFrame")
        main_frame.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_frame, width=420, padding=(15, 15), style="Card.TFrame")
        left_frame.pack(side="left", fill="y")

        right_frame = ttk.Frame(main_frame, width=500, padding=(15, 15), style="Card.TFrame")
        right_frame.pack(side="right", fill="both", expand=True)

        ttk.Label(left_frame, text="Voter Portal", style="Section.TLabel").pack(anchor="w", pady=(0, 10))

        voter_frame = ttk.Frame(left_frame)
        voter_frame.pack(fill="x", pady=(0, 15))

        ttk.Label(voter_frame, text="Voter ID", style="Info.TLabel").grid(row=0, column=0, sticky="w")
        self.voter_entry = ttk.Entry(voter_frame, textvariable=self.voter_id_var, width=30)
        self.voter_entry.grid(row=1, column=0, pady=6, sticky="w")
        self.voter_entry.focus()

        self.constituency_label = ttk.Label(voter_frame, text="Enter voter ID starting with A, B, or C", style="Info.TLabel")
        self.constituency_label.grid(row=2, column=0, sticky="w", pady=(4, 0))

        separator = ttk.Separator(left_frame, orient="horizontal")
        separator.pack(fill="x", pady=15)

        self.candidates_section = ttk.Label(left_frame, text="Select Candidate", style="Section.TLabel")
        self.candidates_section.pack(anchor="w", pady=(0, 10))

        self.candidate_frame = ttk.Frame(left_frame)
        self.candidate_frame.pack(fill="x")

        self.vote_button = ttk.Button(left_frame, text="Cast Vote", command=self.cast_vote)
        self.vote_button.pack(fill="x", pady=(20, 10))

        self.reset_button = ttk.Button(left_frame, text="Reset Form", command=self.reset_form)
        self.reset_button.pack(fill="x")

        ttk.Label(right_frame, text="Dashboard", style="Section.TLabel").pack(anchor="w", pady=(0, 10))

        self.log_text = tk.Text(right_frame, width=56, height=18, wrap="word", bg="#ffffff", fg="#2c3e50", font=("Segoe UI", 10), bd=1, relief="solid")
        self.log_text.pack(fill="both", expand=True)
        self.log_text.insert("end", "Welcome to Secure Blockchain Voting.\nUse the portal to cast your vote and inspect the blockchain.\n")
        self.log_text.configure(state="disabled")

        action_frame = ttk.Frame(right_frame)
        action_frame.pack(fill="x", pady=15)

        self.blockchain_button = ttk.Button(action_frame, text="View Blockchain", command=self.show_blockchain)
        self.blockchain_button.grid(row=0, column=0, padx=4, sticky="ew")

        self.results_button = ttk.Button(action_frame, text="Show Election Results", command=self.show_results)
        self.results_button.grid(row=0, column=1, padx=4, sticky="ew")

        self.commission_button = ttk.Button(action_frame, text="Commission Login", command=self.admin_view)
        self.commission_button.grid(row=0, column=2, padx=4, sticky="ew")

        action_frame.columnconfigure(0, weight=1)
        action_frame.columnconfigure(1, weight=1)
        action_frame.columnconfigure(2, weight=1)

        self.populate_candidates()

    def on_voter_id_change(self, *args):
        voter_id = self.voter_id_var.get().strip()
        if not voter_id:
            self.constituency = None
            self.constituency_label.configure(text="Enter voter ID starting with A, B, or C")
            self.populate_candidates()
            return

        constituency = voter_id[0].upper()
        if constituency not in ["A", "B", "C"]:
            self.constituency = None
            self.constituency_label.configure(text="Invalid constituency. Use A, B, or C.")
            self.populate_candidates()
            return

        self.constituency = constituency
        self.constituency_label.configure(text=f"Constituency: {constituency}")
        self.populate_candidates()

    def populate_candidates(self):
        for widget in self.candidate_frame.winfo_children():
            widget.destroy()

        self.selected_candidate.set("")

        candidates = self.get_candidate_list(self.constituency)
        if not candidates:
            ttk.Label(self.candidate_frame, text="Enter a valid voter ID first.", style="Info.TLabel").pack(anchor="w")
            return

        for candidate_id, candidate_name in candidates.items():
            ttk.Radiobutton(
                self.candidate_frame,
                text=f"{candidate_id}. {candidate_name}",
                value=candidate_id,
                variable=self.selected_candidate,
                style="TRadiobutton",
            ).pack(anchor="w", pady=2)

    def get_candidate_list(self, constituency):
        if constituency == "A":
            return {"1": "Candidate A", "2": "Candidate B", "3": "Candidate C"}
        if constituency == "B":
            return {"1": "Candidate X", "2": "Candidate Y", "3": "Candidate Z"}
        if constituency == "C":
            return {"1": "Candidate D", "2": "Candidate E", "3": "Candidate F"}
        return {}

    def log_message(self, message):
        self.log_text.configure(state="normal")
        self.log_text.insert("end", f"{message}\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

    def cast_vote(self):
        voter_id = self.voter_id_var.get().strip()
        if not voter_id:
            messagebox.showwarning("Missing Voter ID", "Please enter your voter ID.")
            return

        if voter_id in self.blockchain.voter_ids:
            messagebox.showerror("Duplicate Vote", "This voter ID has already been used.")
            return

        if not self.constituency:
            messagebox.showerror("Invalid Voter ID", "Voter ID must start with A, B, or C.")
            return

        candidate_id = self.selected_candidate.get()
        if not candidate_id:
            messagebox.showwarning("Choose Candidate", "Please select a candidate before casting your vote.")
            return

        if not messagebox.askyesno("Confirm Vote", "Do you want to cast your vote now?"):
            return

        vote_data = {"constituency": self.constituency, "candidate_id": candidate_id}
        self.blockchain.new_vote(voter_id, vote_data)
        self.blockchain.increment_candidate_votes(self.constituency, candidate_id)
        self.blockchain.voter_ids.add(voter_id)

        candidate_name = self.get_candidate_list(self.constituency)[candidate_id]
        self.log_message(f"Vote cast for {candidate_name} in constituency {self.constituency}.")
        messagebox.showinfo("Vote Recorded", "Your vote has been recorded successfully.")
        self.reset_form(clear_text=False)

    def reset_form(self, clear_text=True):
        self.voter_id_var.set("")
        self.selected_candidate.set("")
        self.constituency = None
        self.constituency_label.configure(text="Enter voter ID starting with A, B, or C")
        self.populate_candidates()
        if clear_text:
            self.log_text.configure(state="normal")
            self.log_text.delete("1.0", "end")
            self.log_text.insert("end", "Welcome to Secure Blockchain Voting.\nUse the portal to cast your vote and inspect the blockchain.\n")
            self.log_text.configure(state="disabled")

    def show_blockchain(self):
        content = json.dumps(self.blockchain.view_blockchain(), indent=2)
        self.open_text_window("Blockchain Data", content)

    def show_results(self):
        if not self.blockchain.candidates:
            result_text = "No votes have been cast yet."
        else:
            lines = []
            for constituency, votes in self.blockchain.candidates.items():
                lines.append(f"Constituency {constituency}:")
                for candidate_id, info in votes.items():
                    lines.append(f"  {info['name']} (#{candidate_id}) — {info['votes']} votes")
                lines.append("")
            result_text = "\n".join(lines)

        self.open_text_window("Election Results", result_text)

    def admin_view(self):
        login_id = simpledialog.askstring("Commission Login", "Enter Commission Login ID:")
        if login_id != "55":
            messagebox.showerror("Access Denied", "Invalid login ID.")
            return

        constituency = simpledialog.askstring("Constituency", "Enter constituency (A/B/C):")
        if not constituency:
            return

        constituency = constituency.upper()
        results = self.blockchain.election_commission_view(login_id, constituency)
        self.open_text_window("Election Commission View", results)

    def open_text_window(self, title, content):
        window = tk.Toplevel(self.master)
        window.title(title)
        window.geometry("700x520")
        window.configure(bg="#f3f6fb")

        text_widget = tk.Text(window, wrap="word", font=("Segoe UI", 11), bg="#ffffff", fg="#2c3e50", bd=1, relief="solid")
        text_widget.pack(fill="both", expand=True, padx=12, pady=12)
        text_widget.insert("1.0", content)
        text_widget.configure(state="disabled")

        close_button = ttk.Button(window, text="Close", command=window.destroy)
        close_button.pack(pady=(0, 12))


def main():
    root = tk.Tk()
    app = BlockchainGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
