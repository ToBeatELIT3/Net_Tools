syntax on 
filetype on

set number
set noshowmode
set autoindent
set noswapfile
set nomodeline
set laststatus=2
set shiftwidth=4
set colorcolumn=100
set background=dark
set termguicolors
set incsearch

call plug#begin('~/.vim/plugged')

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'itchyny/lightline.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'preservim/nerdtree'
Plug 'dense-analysis/ale'
Plug 'ryanoasis/vim-devicons'

call plug#end()

colorscheme nord

nnoremap <C-t> :below split<cr>:resize 10<cr>:terminal<cr>
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

inoremap jj <Esc>
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
      let col = col('.') - 1
        return !col || getline('.')[col - 1]  =~# '\s'
    endfunction

tnoremap jj <C-\><C-n>
map <C-n> :NERDTreeToggle<CR>

autocmd vimenter * NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif


let g:lightline = {
      \ 'colorscheme': 'nord',
      \ }

