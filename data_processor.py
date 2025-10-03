#!/usr/bin/env python3
"""
Data Processor for Web Application
Structures and optimizes the GitHub issues data for web presentation
"""

import json
import re
from datetime import datetime
from typing import List, Dict, Any
import html

class WebDataProcessor:
    def __init__(self, issues_file: str, analysis_file: str):
        with open(issues_file, 'r', encoding='utf-8') as f:
            self.raw_data = json.load(f)
        
        with open(analysis_file, 'r', encoding='utf-8') as f:
            self.analysis_data = json.load(f)
    
    def clean_markdown_text(self, text: str) -> str:
        """Clean markdown text for better web display"""
        if not text:
            return ""
        
        # Remove excessive whitespace
        text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
        text = text.strip()
        
        # Escape HTML entities
        text = html.escape(text)
        
        return text
    
    def extract_project_info(self, issue_body: str) -> Dict[str, str]:
        """Extract structured project information from issue body"""
        info = {
            'email': '',
            'twitter': '',
            'budget': '',
            'goal': '',
            'team': '',
            'traction': ''
        }
        
        if not issue_body:
            return info
        
        # Extract email
        email_match = re.search(r'[Ee]mail[:\s]*([^\n\r]+)', issue_body)
        if email_match:
            info['email'] = email_match.group(1).strip()
        
        # Extract Twitter
        twitter_match = re.search(r'[Tt]witter[:\s]*([^\n\r]+)', issue_body)
        if twitter_match:
            info['twitter'] = twitter_match.group(1).strip()
        
        # Extract budget
        budget_match = re.search(r'[Bb]udget[:\s]*([^\n\r]+)', issue_body)
        if budget_match:
            info['budget'] = budget_match.group(1).strip()
        
        # Extract goal
        goal_match = re.search(r'[Gg]oal[:\s]*([^\n\r]+)', issue_body)
        if goal_match:
            info['goal'] = goal_match.group(1).strip()
        
        # Extract team
        team_match = re.search(r'[Tt]eam[:\s]*([^\n\r]+)', issue_body)
        if team_match:
            info['team'] = team_match.group(1).strip()
        
        return info
    
    def format_comment_for_display(self, comment: Dict[str, Any]) -> Dict[str, Any]:
        """Format comment for web display"""
        return {
            'id': comment['id'],
            'body': self.clean_markdown_text(comment['body']),
            'body_html': self.markdown_to_html_basic(comment['body']),
            'created_at': comment['created_at'],
            'created_at_formatted': self.format_date(comment['created_at']),
            'html_url': comment['html_url']
        }
    
    def markdown_to_html_basic(self, text: str) -> str:
        """Basic markdown to HTML conversion"""
        if not text:
            return ""
        
        # Escape HTML first
        text = html.escape(text)
        
        # Convert basic markdown
        # Bold
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
        
        # Italic
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
        
        # Code
        text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
        
        # Links
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
        
        # Line breaks
        text = text.replace('\n', '<br>')
        
        return text
    
    def format_date(self, iso_date: str) -> str:
        """Format ISO date for display"""
        try:
            dt = datetime.fromisoformat(iso_date.replace('Z', '+00:00'))
            return dt.strftime('%B %d, %Y at %I:%M %p')
        except:
            return iso_date
    
    def determine_status_badge(self, issue: Dict[str, Any], analysis_summary: Dict[str, Any]) -> Dict[str, str]:
        """Determine status badge for issue"""
        labels = issue.get('labels', [])
        decision_status = analysis_summary.get('decision_status', 'pending')
        
        # Priority order: labels first, then analysis
        if 'Awarded' in labels:
            return {'type': 'success', 'text': 'Awarded', 'color': '#28a745'}
        elif 'In Review' in labels:
            return {'type': 'warning', 'text': 'In Review', 'color': '#ffc107'}
        elif 'Pending Final Applicant Feedback' in labels:
            return {'type': 'info', 'text': 'Pending Feedback', 'color': '#17a2b8'}
        elif 'In Progress' in labels:
            return {'type': 'primary', 'text': 'In Progress', 'color': '#007bff'}
        elif decision_status == 'approved':
            return {'type': 'success', 'text': 'Approved', 'color': '#28a745'}
        elif decision_status == 'rejected':
            return {'type': 'danger', 'text': 'Rejected', 'color': '#dc3545'}
        elif decision_status == 'needs_info':
            return {'type': 'warning', 'text': 'Needs Info', 'color': '#ffc107'}
        else:
            return {'type': 'secondary', 'text': 'Pending', 'color': '#6c757d'}
    
    def process_for_web(self) -> Dict[str, Any]:
        """Process all data for web application"""
        
        # Create lookup for analysis summaries
        analysis_lookup = {s['issue_number']: s for s in self.analysis_data['issue_summaries']}
        
        processed_issues = []
        
        for issue in self.raw_data['issues']:
            analysis_summary = analysis_lookup.get(issue['number'], {})
            project_info = self.extract_project_info(issue['body'])
            
            # Format cuevasm comments
            formatted_comments = [
                self.format_comment_for_display(comment) 
                for comment in issue['cuevasm_comments']
            ]
            
            # Sort comments by date
            formatted_comments.sort(key=lambda x: x['created_at'])
            
            processed_issue = {
                'number': issue['number'],
                'title': issue['title'],
                'body': self.clean_markdown_text(issue['body']),
                'body_html': self.markdown_to_html_basic(issue['body']),
                'body_preview': (issue['body'][:200] + '...') if issue['body'] and len(issue['body']) > 200 else (issue['body'] or ''),
                'state': issue['state'],
                'created_at': issue['created_at'],
                'created_at_formatted': self.format_date(issue['created_at']),
                'updated_at': issue['updated_at'],
                'updated_at_formatted': self.format_date(issue['updated_at']),
                'html_url': issue['html_url'],
                'applicant': {
                    'login': issue['user']['login'],
                    'avatar_url': issue['user']['avatar_url'],
                    'profile_url': f"https://github.com/{issue['user']['login']}"
                },
                'labels': issue['labels'],
                'status_badge': self.determine_status_badge(issue, analysis_summary),
                'project_info': project_info,
                'total_comments': issue['total_comments'],
                'cuevasm_comments': formatted_comments,
                'cuevasm_comment_count': len(formatted_comments),
                'decision_status': analysis_summary.get('decision_status', 'pending'),
                'has_cuevasm_comments': len(formatted_comments) > 0,
                'latest_cuevasm_comment': formatted_comments[-1] if formatted_comments else None,
                'cuevasm_activity_summary': self.generate_activity_summary(formatted_comments)
            }
            
            processed_issues.append(processed_issue)
        
        # Sort issues by number (descending for newest first)
        processed_issues.sort(key=lambda x: x['number'], reverse=True)
        
        # Generate summary statistics
        summary_stats = {
            'total_issues': len(processed_issues),
            'awarded_count': len([i for i in processed_issues if i['status_badge']['type'] == 'success']),
            'in_review_count': len([i for i in processed_issues if i['status_badge']['type'] == 'warning']),
            'pending_count': len([i for i in processed_issues if i['status_badge']['type'] == 'secondary']),
            'total_cuevasm_comments': sum(i['cuevasm_comment_count'] for i in processed_issues),
            'issues_with_cuevasm_comments': len([i for i in processed_issues if i['has_cuevasm_comments']]),
            'last_updated': max([i['updated_at'] for i in processed_issues]) if processed_issues else None
        }
        
        return {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'repository': self.raw_data['repository'],
                'target_user': self.raw_data['target_user'],
                'data_source': 'GitHub REST API',
                'version': '1.0'
            },
            'summary': summary_stats,
            'issues': processed_issues,
            'analysis_insights': {
                'top_keywords': list(self.analysis_data['comment_patterns']['keyword_frequency'].items())[:10],
                'comment_categories': self.analysis_data['comment_categories'],
                'decision_breakdown': self.analysis_data['decision_analysis']
            }
        }
    
    def generate_activity_summary(self, comments: List[Dict[str, Any]]) -> str:
        """Generate a summary of cuevasm's activity on the issue"""
        if not comments:
            return "No comments from cuevasm"
        
        count = len(comments)
        if count == 1:
            return "1 comment from cuevasm"
        else:
            latest_date = self.format_date(comments[-1]['created_at'])
            return f"{count} comments from cuevasm, latest on {latest_date}"

def main():
    processor = WebDataProcessor(
        '/home/ubuntu/github_issues_data.json',
        '/home/ubuntu/cuevasm_analysis_report.json'
    )
    
    web_data = processor.process_for_web()
    
    # Save processed data
    output_file = '/home/ubuntu/web_app_data.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(web_data, f, indent=2, ensure_ascii=False)
    
    print("=== WEB DATA PROCESSING COMPLETE ===")
    print(f"Processed {web_data['summary']['total_issues']} issues")
    print(f"Total cuevasm comments: {web_data['summary']['total_cuevasm_comments']}")
    print(f"Issues with cuevasm comments: {web_data['summary']['issues_with_cuevasm_comments']}")
    print(f"\nStatus breakdown:")
    print(f"  Awarded: {web_data['summary']['awarded_count']}")
    print(f"  In Review: {web_data['summary']['in_review_count']}")
    print(f"  Pending: {web_data['summary']['pending_count']}")
    print(f"\nData saved to: {output_file}")

if __name__ == "__main__":
    main()
