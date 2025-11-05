import pandas as pd
import matplotlib.pyplot as plt
jobs=pd.read_csv("jobs.csv")
def normalize_skills(skills_str):
    return set(
       skill.strip().lower() 
       for skill in skills_str.replace(",","|").replace(" ","|").split("|")
       if skill.strip()
       )
def match_jobs(user):
    matched_jobs=[]
    user_skills= normalize_skills(user["Skills"])
    user_location=user["Location"].strip().lower()
    user_experience=int(user["Experience"])

    for _,job in jobs.iterrows():
        job_skills=normalize_skills(job["Required Skills"])
        skill_match= len(user_skills.intersection(job_skills))
        location_match= int(user_location == job["Location"].strip().lower())
        experience_match= user_experience >= float(job["Experience"])
        match_score=(skill_match*2)+ location_match

        if skill_match>0 and experience_match:
            matched_jobs.append({
                "Job Title":job["Job Title"],
                "Match Score":match_score,
                "Skills Matched":list(user_skills.intersection(job_skills))
            })

    matched_jobs=sorted(matched_jobs, key=lambda x:x["Match Score"],reverse=True)
    return matched_jobs[:3] if matched_jobs else[{
               "Job Title":"No match found",
               "Match Score":0,
               "Skills Matched":[]
               }]
name= input("Enter your name: ").strip()
skills= input("Enter your skills(eg: Python,SQL,ML): ").strip()
location= input("Enter your location: ").strip()
experience= int(input("Enter your experience(in years): ").strip())

user={"Name":name,"Skills":skills,"Location":location,"Experience":experience}

matches=match_jobs(user)

matches_df=pd.DataFrame(matches)
matches_df["User"]=name
matches_df=matches_df[["User","Job Title","Match Score","Skills Matched"]]

print("\nTop job matches for you:\n")
print(matches_df)

matches_df.to_csv("matched_results.csv",index=False)
print("\nResults saved to 'matched_results.csv'")
valid_matches= matches_df[matches_df["Job Title"]!="No match found"]

if not valid_matches.empty: 
         plt.bar(valid_matches["Job Title"],valid_matches["Match Score"],color='mediumseagreen')
         plt.title(f"Top Matches {name}")
         plt.ylabel("Match score")
         plt.xlabel("Job Title")
         plt.xticks(rotation=15)
         plt.tight_layout()
         plt.show()
else:
     print("No suitable jobs found to visualize.")

