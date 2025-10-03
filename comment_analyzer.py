#!/usr/bin/env python3
"""
Comment Analyzer for cuevasm's GitHub Comments
Processes and analyzes cuevasm's comments to extract insights and patterns
"""

import json
import re
from datetime import datetime
from typing import List, Dict, Any
from collections import Counter

class CommentAnalyzer:
    def __init__(self, data_file: str):
        with open(data_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        
        self.issues = self.data['issues']
        self.cuevasm_comments = self._extract_all_cuevasm_comments()
    
    def _extract_all_cuevasm_comments(self) -> List[Dict[str, Any]]:
        """Extract all cuevasm comments with issue context"""
        all_comments = []
        
        for issue in self.issues:
            for comment in issue['cuevasm_comments']:
                comment_with_context = {
                    **comment,
                    'issue_number': issue['number'],
                    'issue_title': issue['title'],
                    'issue_state': issue['state'],
                    'issue_labels': issue['labels']
                }
                all_comments.append(comment_with_context)
        
        return all_comments
    
    def analyze_comment_patterns(self) -> Dict[str, Any]:
        """Analyze patterns in cuevasm's comments"""
        
        # Keywords analysis
        all_text = ' '.join([comment['body'].lower() for comment in self.cuevasm_comments])
        
        # Common decision-making keywords
        decision_keywords = [
            'approved', 'denied', 'rejected', 'accepted', 'awarded', 'granted',
            'needs', 'requires', 'missing', 'incomplete', 'complete',
            'good', 'excellent', 'strong', 'weak', 'concerns', 'issues',
            'budget', 'funding', 'amount', 'timeline', 'milestone',
            'team', 'experience', 'track record', 'previous work',
            'impact', 'value', 'benefit', 'risk', 'feasible'
        ]
        
        keyword_counts = {}
        for keyword in decision_keywords:
            count = all_text.count(keyword)
            if count > 0:
                keyword_counts[keyword] = count
        
        # Comment length analysis
        comment_lengths = [len(comment['body']) for comment in self.cuevasm_comments]
        avg_length = sum(comment_lengths) / len(comment_lengths) if comment_lengths else 0
        
        # Temporal analysis
        comment_dates = [datetime.fromisoformat(comment['created_at'].replace('Z', '+00:00')) 
                        for comment in self.cuevasm_comments]
        
        if comment_dates:
            earliest = min(comment_dates)
            latest = max(comment_dates)
            date_range = (latest - earliest).days
        else:
            earliest = latest = None
            date_range = 0
        
        return {
            'total_comments': len(self.cuevasm_comments),
            'keyword_frequency': dict(sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)),
            'average_comment_length': round(avg_length, 2),
            'comment_length_range': {
                'min': min(comment_lengths) if comment_lengths else 0,
                'max': max(comment_lengths) if comment_lengths else 0
            },
            'temporal_analysis': {
                'earliest_comment': earliest.isoformat() if earliest else None,
                'latest_comment': latest.isoformat() if latest else None,
                'activity_span_days': date_range
            }
        }
    
    def categorize_comments(self) -> Dict[str, List[Dict[str, Any]]]:
        """Categorize comments by type/intent"""
        categories = {
            'approvals': [],
            'rejections': [],
            'requests_for_info': [],
            'feedback': [],
            'status_updates': [],
            'questions': [],
            'other': []
        }
        
        for comment in self.cuevasm_comments:
            body_lower = comment['body'].lower()
            
            # Approval indicators
            if any(word in body_lower for word in ['approved', 'awarded', 'granted', 'accepted', 'looks good', 'lgtm']):
                categories['approvals'].append(comment)
            
            # Rejection indicators
            elif any(word in body_lower for word in ['rejected', 'denied', 'not approved', 'cannot approve']):
                categories['rejections'].append(comment)
            
            # Request for information
            elif any(word in body_lower for word in ['need more', 'please provide', 'missing', 'incomplete', 'clarify']):
                categories['requests_for_info'].append(comment)
            
            # Questions
            elif '?' in comment['body'] or any(word in body_lower for word in ['what', 'how', 'when', 'where', 'why']):
                categories['questions'].append(comment)
            
            # Status updates
            elif any(word in body_lower for word in ['update', 'progress', 'status', 'milestone', 'completed']):
                categories['status_updates'].append(comment)
            
            # Feedback
            elif any(word in body_lower for word in ['feedback', 'suggestion', 'recommend', 'consider', 'think']):
                categories['feedback'].append(comment)
            
            else:
                categories['other'].append(comment)
        
        return categories
    
    def generate_issue_summaries(self) -> List[Dict[str, Any]]:
        """Generate summaries for each issue with cuevasm's involvement"""
        summaries = []
        
        for issue in self.issues:
            if issue['cuevasm_comment_count'] > 0:
                # Analyze cuevasm's comments for this issue
                comments = issue['cuevasm_comments']
                
                # Determine decision status
                decision_status = 'pending'
                latest_comment = max(comments, key=lambda x: x['created_at'])
                latest_body = latest_comment['body'].lower()
                
                if any(word in latest_body for word in ['approved', 'awarded', 'granted']):
                    decision_status = 'approved'
                elif any(word in latest_body for word in ['rejected', 'denied']):
                    decision_status = 'rejected'
                elif any(word in latest_body for word in ['need more', 'missing', 'incomplete']):
                    decision_status = 'needs_info'
                
                # Extract key themes from comments
                all_comment_text = ' '.join([c['body'] for c in comments])
                
                summary = {
                    'issue_number': issue['number'],
                    'title': issue['title'],
                    'state': issue['state'],
                    'labels': issue['labels'],
                    'applicant': issue['user']['login'],
                    'cuevasm_comment_count': issue['cuevasm_comment_count'],
                    'decision_status': decision_status,
                    'latest_cuevasm_comment': latest_comment,
                    'first_cuevasm_comment': min(comments, key=lambda x: x['created_at']),
                    'comment_summary': all_comment_text[:200] + '...' if len(all_comment_text) > 200 else all_comment_text,
                    'html_url': issue['html_url']
                }
                
                summaries.append(summary)
        
        return sorted(summaries, key=lambda x: x['issue_number'])
    
    def generate_analysis_report(self) -> Dict[str, Any]:
        """Generate comprehensive analysis report"""
        patterns = self.analyze_comment_patterns()
        categories = self.categorize_comments()
        summaries = self.generate_issue_summaries()
        
        # Category statistics
        category_stats = {cat: len(comments) for cat, comments in categories.items()}
        
        # Decision statistics
        decision_stats = Counter([s['decision_status'] for s in summaries])
        
        report = {
            'analysis_date': datetime.now().isoformat(),
            'overview': {
                'total_issues_analyzed': len(self.issues),
                'issues_with_cuevasm_comments': len([i for i in self.issues if i['cuevasm_comment_count'] > 0]),
                'total_cuevasm_comments': patterns['total_comments']
            },
            'comment_patterns': patterns,
            'comment_categories': category_stats,
            'decision_analysis': dict(decision_stats),
            'issue_summaries': summaries,
            'detailed_categories': categories
        }
        
        return report

def main():
    analyzer = CommentAnalyzer('/home/ubuntu/github_issues_data.json')
    report = analyzer.generate_analysis_report()
    
    # Save analysis report
    output_file = '/home/ubuntu/cuevasm_analysis_report.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("=== CUEVASM COMMENT ANALYSIS ===")
    print(f"Total issues: {report['overview']['total_issues_analyzed']}")
    print(f"Issues with cuevasm comments: {report['overview']['issues_with_cuevasm_comments']}")
    print(f"Total cuevasm comments: {report['overview']['total_cuevasm_comments']}")
    print(f"\nDecision breakdown:")
    for status, count in report['decision_analysis'].items():
        print(f"  {status}: {count}")
    
    print(f"\nComment categories:")
    for category, count in report['comment_categories'].items():
        print(f"  {category}: {count}")
    
    print(f"\nTop keywords:")
    for keyword, count in list(report['comment_patterns']['keyword_frequency'].items())[:10]:
        print(f"  {keyword}: {count}")
    
    print(f"\nAnalysis report saved to: {output_file}")

if __name__ == "__main__":
    main()
