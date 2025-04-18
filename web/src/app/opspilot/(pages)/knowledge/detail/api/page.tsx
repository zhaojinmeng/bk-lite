import React from 'react';
import MarkdownRenderer from '@/components/markdown';

const MarkdownPage: React.FC = () => {
  return (
    <div>
      <MarkdownRenderer filePath="module_api/" fileName="knowledge_api" />
    </div>
  );
};

export default MarkdownPage;
