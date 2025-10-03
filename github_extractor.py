#!/usr/bin/env python3
"""
GitHub Issues and Comments Extractor
Extracts all issues and comments from stacksgov/sip31-interim-grants repository
Focuses on comments by cuevasm user
"""

import requests
import json
import time
from typing import List, Dict, Any

class GitHubExtractor:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.owner = "stacksgov"
        self.repo = "sip31-interim-grants"
        self.target_user = "cuevasm"
        self.session = requests.Session()
        
        # Set headers for better API response
        self.session.headers.update({
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        })
    
    def get_all_issues(self) -> List[Dict[str, Any]]:
        """Get all issues (both open and closed) from the repository"""
        all_issues = []
        
        # Get open issues
        open_issues = self._get_issues_by_state('open')
        all_issues.extend(open_issues)
        
        # Get closed issues
        closed_issues = self._get_issues_by_state('closed')
        all_issues.extend(closed_issues)
        
        print(f"Total issues found: {len(all_issues)}")
        return all_issues
    
    def _get_issues_by_state(self, state: str) -> List[Dict[str, Any]]:
        """Get issues by state (open/closed) with pagination"""
        issues = []
        page = 1
        per_page = 100
        
        while True:
            url = f"{self.base_url}/repos/{self.owner}/{self.repo}/issues"
            params = {
                'state': state,
                'page': page,
                'per_page': per_page,
                'sort': 'created',
                'direction': 'asc'
            }
            
            print(f"Fetching {state} issues page {page}...")
            response = self.session.get(url, params=params)
            
            if response.status_code != 200:
                print(f"Error fetching issues: {response.status_code}")
                break
            
            page_issues = response.json()
            
            if not page_issues:
                break
            
            # Filter out pull requests (they have pull_request key)
            actual_issues = [issue for issue in page_issues if 'pull_request' not in issue]
            issues.extend(actual_issues)
            
            print(f"Found {len(actual_issues)} issues on page {page}")
            
            if len(page_issues) < per_page:
                break
            
            page += 1
            time.sleep(0.1)  # Rate limiting
        
        return issues
    
    def get_issue_comments(self, issue_number: int) -> List[Dict[str, Any]]:
        """Get all comments for a specific issue"""
        comments = []
        page = 1
        per_page = 100
        
        while True:
            url = f"{self.base_url}/repos/{self.owner}/{self.repo}/issues/{issue_number}/comments"
            params = {
                'page': page,
                'per_page': per_page
            }
            
            response = self.session.get(url, params=params)
            
            if response.status_code != 200:
                print(f"Error fetching comments for issue #{issue_number}: {response.status_code}")
                break
            
            page_comments = response.json()
            
            if not page_comments:
                break
            
            comments.extend(page_comments)
            
            if len(page_comments) < per_page:
                break
            
            page += 1
            time.sleep(0.1)  # Rate limiting
        
        return comments
    
    def extract_cuevasm_comments(self, comments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter comments to only include those by cuevasm"""
        cuevasm_comments = []
        
        for comment in comments:
            if comment.get('user', {}).get('login') == self.target_user:
                cuevasm_comments.append({
                    'id': comment['id'],
                    'body': comment['body'],
                    'created_at': comment['created_at'],
                    'updated_at': comment['updated_at'],
                    'html_url': comment['html_url']
                })
        
        return cuevasm_comments
    
    def extract_all_data(self) -> Dict[str, Any]:
        """Extract all issues and cuevasm's comments"""
        print("Starting data extraction...")
        
        # Get all issues
        issues = self.get_all_issues()
        
        # Process each issue
        processed_issues = []
        
        for issue in issues:
            issue_number = issue['number']
            print(f"\nProcessing issue #{issue_number}: {issue['title'][:50]}...")
            
            # Get comments for this issue
            comments = self.get_issue_comments(issue_number)
            cuevasm_comments = self.extract_cuevasm_comments(comments)
            
            # Process issue data
            processed_issue = {
                'number': issue['number'],
                'title': issue['title'],
                'body': issue['body'],
                'state': issue['state'],
                'created_at': issue['created_at'],
                'updated_at': issue['updated_at'],
                'html_url': issue['html_url'],
                'user': {
                    'login': issue['user']['login'],
                    'avatar_url': issue['user']['avatar_url']
                },
                'labels': [label['name'] for label in issue.get('labels', [])],
                'total_comments': len(comments),
                'cuevasm_comments': cuevasm_comments,
                'cuevasm_comment_count': len(cuevasm_comments)
            }
            
            processed_issues.append(processed_issue)
            print(f"  - Total comments: {len(comments)}")
            print(f"  - cuevasm comments: {len(cuevasm_comments)}")
        
        # Summary statistics
        total_cuevasm_comments = sum(issue['cuevasm_comment_count'] for issue in processed_issues)
        issues_with_cuevasm_comments = len([issue for issue in processed_issues if issue['cuevasm_comment_count'] > 0])
        
        result = {
            'extraction_date': time.strftime('%Y-%m-%d %H:%M:%S'),
            'repository': f"{self.owner}/{self.repo}",
            'target_user': self.target_user,
            'summary': {
                'total_issues': len(processed_issues),
                'total_cuevasm_comments': total_cuevasm_comments,
                'issues_with_cuevasm_comments': issues_with_cuevasm_comments
            },
            'issues': processed_issues
        }
        
        return result

def main():
    extractor = GitHubExtractor()
    data = extractor.extract_all_data()
    
    # Save to JSON file
    output_file = '/home/ubuntu/github_issues_data.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n=== EXTRACTION COMPLETE ===")
    print(f"Data saved to: {output_file}")
    print(f"Total issues: {data['summary']['total_issues']}")
    print(f"Total cuevasm comments: {data['summary']['total_cuevasm_comments']}")
    print(f"Issues with cuevasm comments: {data['summary']['issues_with_cuevasm_comments']}")

if __name__ == "__main__":
    main()
