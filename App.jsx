import { useState, useEffect } from 'react'
import { Search, Filter, ExternalLink, MessageSquare, Calendar, User, Award, Clock, AlertCircle } from 'lucide-react'
import { Button } from '@/components/ui/button.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar.jsx'
import { Separator } from '@/components/ui/separator.jsx'
import { motion, AnimatePresence } from 'framer-motion'
import './App.css'
import data from './assets/data.json'

function App() {
  const [issues, setIssues] = useState([])
  const [filteredIssues, setFilteredIssues] = useState([])
  const [searchTerm, setSearchTerm] = useState('')
  const [statusFilter, setStatusFilter] = useState('all')
  const [selectedIssue, setSelectedIssue] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Simulate loading and set data
    setTimeout(() => {
      setIssues(data.issues)
      setFilteredIssues(data.issues)
      setLoading(false)
    }, 500)
  }, [])

  useEffect(() => {
    let filtered = issues

    // Filter by search term
    if (searchTerm) {
      filtered = filtered.filter(issue =>
        issue.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        issue.applicant.login.toLowerCase().includes(searchTerm.toLowerCase()) ||
        issue.project_info.goal.toLowerCase().includes(searchTerm.toLowerCase())
      )
    }

    // Filter by status
    if (statusFilter !== 'all') {
      filtered = filtered.filter(issue => {
        switch (statusFilter) {
          case 'awarded':
            return issue.status_badge.type === 'success'
          case 'in-review':
            return issue.status_badge.type === 'warning'
          case 'pending':
            return issue.status_badge.type === 'secondary'
          case 'with-comments':
            return issue.has_cuevasm_comments
          default:
            return true
        }
      })
    }

    setFilteredIssues(filtered)
  }, [issues, searchTerm, statusFilter])

  const getStatusBadgeVariant = (type) => {
    switch (type) {
      case 'success': return 'default'
      case 'warning': return 'secondary'
      case 'info': return 'outline'
      case 'primary': return 'default'
      case 'danger': return 'destructive'
      default: return 'secondary'
    }
  }

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    })
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-slate-900 mx-auto mb-4"></div>
          <p className="text-slate-600">Loading SIP31 grants data...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
      {/* Header */}
      <header className="bg-white border-b border-slate-200 sticky top-0 z-50 backdrop-blur-sm bg-white/95">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2">
                <Award className="h-8 w-8 text-orange-600" />
                <div>
                  <h1 className="text-xl font-bold text-slate-900">SIP31 Interim Grants</h1>
                  <p className="text-sm text-slate-600">cuevasm's Comments & Decisions</p>
                </div>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Badge variant="outline" className="hidden sm:flex">
                {data.summary.total_issues} Issues
              </Badge>
              <Badge variant="outline" className="hidden sm:flex">
                {data.summary.total_cuevasm_comments} Comments
              </Badge>
            </div>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Summary Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <Card>
            <CardContent className="p-6">
              <div className="flex items-center">
                <Award className="h-8 w-8 text-green-600" />
                <div className="ml-4">
                  <p className="text-sm font-medium text-slate-600">Awarded</p>
                  <p className="text-2xl font-bold text-slate-900">{data.summary.awarded_count}</p>
                </div>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="p-6">
              <div className="flex items-center">
                <Clock className="h-8 w-8 text-yellow-600" />
                <div className="ml-4">
                  <p className="text-sm font-medium text-slate-600">In Review</p>
                  <p className="text-2xl font-bold text-slate-900">{data.summary.in_review_count}</p>
                </div>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="p-6">
              <div className="flex items-center">
                <AlertCircle className="h-8 w-8 text-slate-600" />
                <div className="ml-4">
                  <p className="text-sm font-medium text-slate-600">Pending</p>
                  <p className="text-2xl font-bold text-slate-900">{data.summary.pending_count}</p>
                </div>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="p-6">
              <div className="flex items-center">
                <MessageSquare className="h-8 w-8 text-blue-600" />
                <div className="ml-4">
                  <p className="text-sm font-medium text-slate-600">Total Comments</p>
                  <p className="text-2xl font-bold text-slate-900">{data.summary.total_cuevasm_comments}</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Filters */}
        <Card className="mb-8">
          <CardContent className="p-6">
            <div className="flex flex-col sm:flex-row gap-4">
              <div className="flex-1">
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400 h-4 w-4" />
                  <Input
                    placeholder="Search by title, applicant, or goal..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="pl-10"
                  />
                </div>
              </div>
              <div className="flex gap-2">
                <Button
                  variant={statusFilter === 'all' ? 'default' : 'outline'}
                  onClick={() => setStatusFilter('all')}
                  size="sm"
                >
                  All
                </Button>
                <Button
                  variant={statusFilter === 'awarded' ? 'default' : 'outline'}
                  onClick={() => setStatusFilter('awarded')}
                  size="sm"
                >
                  Awarded
                </Button>
                <Button
                  variant={statusFilter === 'in-review' ? 'default' : 'outline'}
                  onClick={() => setStatusFilter('in-review')}
                  size="sm"
                >
                  In Review
                </Button>
                <Button
                  variant={statusFilter === 'pending' ? 'default' : 'outline'}
                  onClick={() => setStatusFilter('pending')}
                  size="sm"
                >
                  Pending
                </Button>
                <Button
                  variant={statusFilter === 'with-comments' ? 'default' : 'outline'}
                  onClick={() => setStatusFilter('with-comments')}
                  size="sm"
                >
                  With Comments
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Issues Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <AnimatePresence>
            {filteredIssues.map((issue) => (
              <motion.div
                key={issue.number}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
                transition={{ duration: 0.3 }}
              >
                <Card className="hover:shadow-lg transition-shadow cursor-pointer" onClick={() => setSelectedIssue(issue)}>
                  <CardHeader>
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center gap-2 mb-2">
                          <Badge variant="outline" className="text-xs">#{issue.number}</Badge>
                          <Badge 
                            variant={getStatusBadgeVariant(issue.status_badge.type)}
                            style={{ backgroundColor: issue.status_badge.color, color: 'white' }}
                          >
                            {issue.status_badge.text}
                          </Badge>
                        </div>
                        <CardTitle className="text-lg leading-tight mb-2">{issue.title}</CardTitle>
                        <CardDescription className="line-clamp-2">
                          {issue.project_info.goal || issue.body_preview}
                        </CardDescription>
                      </div>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="flex items-center justify-between mb-4">
                      <div className="flex items-center space-x-2">
                        <Avatar className="h-6 w-6">
                          <AvatarImage src={issue.applicant.avatar_url} />
                          <AvatarFallback>{issue.applicant.login[0].toUpperCase()}</AvatarFallback>
                        </Avatar>
                        <span className="text-sm text-slate-600">{issue.applicant.login}</span>
                      </div>
                      <div className="flex items-center space-x-2 text-sm text-slate-500">
                        <Calendar className="h-4 w-4" />
                        <span>{formatDate(issue.created_at)}</span>
                      </div>
                    </div>
                    
                    {issue.has_cuevasm_comments && (
                      <div className="bg-blue-50 rounded-lg p-3">
                        <div className="flex items-center space-x-2 mb-2">
                          <MessageSquare className="h-4 w-4 text-blue-600" />
                          <span className="text-sm font-medium text-blue-900">cuevasm's Activity</span>
                        </div>
                        <p className="text-sm text-blue-800">{issue.cuevasm_activity_summary}</p>
                        {issue.latest_cuevasm_comment && (
                          <p className="text-xs text-blue-600 mt-2 line-clamp-2">
                            "{issue.latest_cuevasm_comment.body.substring(0, 100)}..."
                          </p>
                        )}
                      </div>
                    )}
                    
                    <div className="flex items-center justify-between mt-4">
                      <div className="flex items-center space-x-4 text-sm text-slate-500">
                        <span className="flex items-center space-x-1">
                          <MessageSquare className="h-4 w-4" />
                          <span>{issue.total_comments}</span>
                        </span>
                        {issue.cuevasm_comment_count > 0 && (
                          <span className="flex items-center space-x-1 text-blue-600">
                            <User className="h-4 w-4" />
                            <span>{issue.cuevasm_comment_count} from cuevasm</span>
                          </span>
                        )}
                      </div>
                      <Button variant="ghost" size="sm">
                        <ExternalLink className="h-4 w-4" />
                      </Button>
                    </div>
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>

        {filteredIssues.length === 0 && (
          <div className="text-center py-12">
            <AlertCircle className="h-12 w-12 text-slate-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-slate-900 mb-2">No issues found</h3>
            <p className="text-slate-600">Try adjusting your search or filter criteria.</p>
          </div>
        )}
      </div>

      {/* Issue Detail Modal */}
      {selectedIssue && (
        <IssueDetailModal 
          issue={selectedIssue} 
          onClose={() => setSelectedIssue(null)} 
        />
      )}
    </div>
  )
}

// Issue Detail Modal Component
function IssueDetailModal({ issue, onClose }) {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        exit={{ opacity: 0, scale: 0.95 }}
        className="bg-white rounded-lg max-w-4xl w-full max-h-[90vh] overflow-hidden"
      >
        <div className="flex items-center justify-between p-6 border-b">
          <div>
            <div className="flex items-center gap-2 mb-2">
              <Badge variant="outline">#{issue.number}</Badge>
              <Badge 
                variant="default"
                style={{ backgroundColor: issue.status_badge.color, color: 'white' }}
              >
                {issue.status_badge.text}
              </Badge>
            </div>
            <h2 className="text-xl font-bold">{issue.title}</h2>
          </div>
          <Button variant="ghost" onClick={onClose}>
            ×
          </Button>
        </div>
        
        <div className="overflow-y-auto max-h-[calc(90vh-120px)]">
          <div className="p-6">
            <Tabs defaultValue="overview" className="w-full">
              <TabsList className="grid w-full grid-cols-3">
                <TabsTrigger value="overview">Overview</TabsTrigger>
                <TabsTrigger value="comments">cuevasm's Comments ({issue.cuevasm_comment_count})</TabsTrigger>
                <TabsTrigger value="details">Project Details</TabsTrigger>
              </TabsList>
              
              <TabsContent value="overview" className="mt-6">
                <div className="space-y-6">
                  <div className="flex items-center space-x-4">
                    <Avatar className="h-10 w-10">
                      <AvatarImage src={issue.applicant.avatar_url} />
                      <AvatarFallback>{issue.applicant.login[0].toUpperCase()}</AvatarFallback>
                    </Avatar>
                    <div>
                      <p className="font-medium">{issue.applicant.login}</p>
                      <p className="text-sm text-slate-600">Applied on {new Date(issue.created_at).toLocaleDateString()}</p>
                    </div>
                  </div>
                  
                  <div>
                    <h3 className="font-semibold mb-2">Project Description</h3>
                    <div 
                      className="prose prose-sm max-w-none"
                      dangerouslySetInnerHTML={{ __html: issue.body_html }}
                    />
                  </div>
                </div>
              </TabsContent>
              
              <TabsContent value="comments" className="mt-6">
                <div className="space-y-4">
                  {issue.cuevasm_comments.length > 0 ? (
                    issue.cuevasm_comments.map((comment) => (
                      <Card key={comment.id}>
                        <CardContent className="p-4">
                          <div className="flex items-center justify-between mb-3">
                            <div className="flex items-center space-x-2">
                              <Avatar className="h-6 w-6">
                                <AvatarFallback>CM</AvatarFallback>
                              </Avatar>
                              <span className="font-medium text-sm">cuevasm</span>
                            </div>
                            <span className="text-xs text-slate-500">{comment.created_at_formatted}</span>
                          </div>
                          <div 
                            className="prose prose-sm max-w-none"
                            dangerouslySetInnerHTML={{ __html: comment.body_html }}
                          />
                        </CardContent>
                      </Card>
                    ))
                  ) : (
                    <p className="text-slate-600 text-center py-8">No comments from cuevasm yet.</p>
                  )}
                </div>
              </TabsContent>
              
              <TabsContent value="details" className="mt-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {issue.project_info.budget && (
                    <div>
                      <h4 className="font-semibold mb-2">Budget</h4>
                      <p className="text-slate-600">{issue.project_info.budget}</p>
                    </div>
                  )}
                  {issue.project_info.team && (
                    <div>
                      <h4 className="font-semibold mb-2">Team</h4>
                      <p className="text-slate-600">{issue.project_info.team}</p>
                    </div>
                  )}
                  {issue.project_info.email && (
                    <div>
                      <h4 className="font-semibold mb-2">Contact Email</h4>
                      <p className="text-slate-600">{issue.project_info.email}</p>
                    </div>
                  )}
                  {issue.project_info.twitter && (
                    <div>
                      <h4 className="font-semibold mb-2">Twitter</h4>
                      <p className="text-slate-600">{issue.project_info.twitter}</p>
                    </div>
                  )}
                  <div>
                    <h4 className="font-semibold mb-2">GitHub Issue</h4>
                    <a 
                      href={issue.html_url} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="text-blue-600 hover:underline flex items-center space-x-1"
                    >
                      <span>View on GitHub</span>
                      <ExternalLink className="h-4 w-4" />
                    </a>
                  </div>
                  <div>
                    <h4 className="font-semibold mb-2">Labels</h4>
                    <div className="flex flex-wrap gap-2">
                      {issue.labels.map((label) => (
                        <Badge key={label} variant="outline" className="text-xs">
                          {label}
                        </Badge>
                      ))}
                    </div>
                  </div>
                </div>
              </TabsContent>
            </Tabs>
          </div>
        </div>
      </motion.div>
    </div>
  )
}

export default App
